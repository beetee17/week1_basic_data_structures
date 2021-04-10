# python3

from collections import namedtuple
from queue import Queue

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_times = Queue(maxsize=size)
        

    def process(self, request):
        """You are given a series of incoming network packets, and your task is to simulate their processing.Packets arrive in some order. For each packet number 𝑖, you know the time when it arrived 𝐴𝑖 and the time it takes the processor to process it 𝑃𝑖(both in milliseconds). There is only one processor, and it processes the incoming packets in the order of their arrival. If the processor started to process some packet, it doesn’t interrupt or stop until it finishes the processing of this packet.
        
        The computer processing the packets has a network buffer of fixed size 𝑆. When packets ar-rive, they are stored in the buffer before being processed. However, if the buffer is full when a packet arrives (there are 𝑆 packets which have arrived before this packet, and the computer hasn’t finished processing any of them), it is dropped and won’t be processed at all. 
        
        If several packets arrive at the same time, they are first all stored in the buffer (some of them may be dropped). Note that a packet leaves the bufferand frees the space in the buffer as soon as the computer finishes processing it.
        
        Input Format
        The first line of the input contains the size 𝑆 of the buffer and the number 𝑛 of incoming network packets. Each of the next 𝑛 lines contains two numbers.
        
        The 𝑖-th line contains the time of arrival 𝐴𝑖 and the processing time 𝑃𝑖 (both in milliseconds) of the 𝑖-th packet. 
        
        It is guaranteed that thesequence of arrival times is non-decreasing (however, it can contain the exact same times of arrival in milliseconds — in this case the packet which is earlier in the input is considered to have arrived earlier).
        
        Constraints
        All the numbers in the input are integers
        1 ≤ 𝑆 ≤ 10^5
        0 ≤ 𝑛 ≤ 10^5
        0 ≤ 𝐴𝑖 ≤ 10^6
        0 ≤ 𝑃𝑖 ≤ 10^3
        𝐴𝑖 ≤ 𝐴𝑖+1 for 1 ≤ 𝑖 ≤ 𝑛−1
        
        Output Format
        For each packet output either the moment of time (in milliseconds) when the processorbegan processing it or −1 if the packet was dropped (output the answers for the packets in the same order as the packets are given in the input)"""

        # One possible solution is to store in a queue finish_times, the times when the computer will finish processing the packets which are currently stored in the network buffer, in increasing order. 
        
        # When a new packet arrives, you will first need to pop from the front of finish_times all the packets which are already processed by the time new packet arrives. 
        

        while not self.finish_times.empty():
            if self.finish_times.queue[0] <= request.arrived_at:
                self.finish_times.get_nowait()
            else:
                break
            

        # If finish_times is empty when a new packet arrives, computer will start processing the new packet immediately as soon as it arrives.
        
        if self.finish_times.empty():
            self.finish_times.put_nowait(request.arrived_at + request.time_to_process)
            return Response(False, request.arrived_at)

        # If the buffer is full (there are already 𝑆 finish times in finish_times), the packet is dropped. 
        if self.finish_times.full():
            return Response(True, -1)

        
        else:
        # Otherwise, computer will start processing the new packet as soon as it finishes to process the last of the packets currently in finish_times(here is when you need to access the last element of finish_times to determine when the computer will start to process the new packet). 
        
        # You will also need to compute the processing finish time by adding 𝑃𝑖 to the processing start time and push it to the back of finish_times.
            finish_time = self.finish_times.queue[-1] + request.time_to_process
            self.finish_times.put_nowait(finish_time)
            return Response(False, finish_time - request.time_to_process)

def process_requests(requests, buffer):
    responses = []
    for request in requests:
        response = buffer.process(request)
        responses.append(response)
        # print(responses)
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)
    
    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
