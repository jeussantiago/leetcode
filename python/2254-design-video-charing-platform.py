'''
    - have a current id counter
    - if a video is deleted
        - recycle the id by throwing it into a minHeap
    
    upload:
        - if the minHeap is Not empty:
            - the current id for the video is the item from top of minHeap
            - pop item from minHeap
        - otherwise
            - video id is going to be the current number counter
            - increase id counter
        
        Time: O(logn)
            ; remove from heap

    Remove:
        - if the id exist:
            - push the id onto a minHeap
            - delete the key, val from the dict

        Time: O(logn)
            ; push onto heap

'''


class Video:
    def __init__(self, content):
        self.content = content
        self.likes = 0
        self.dislikes = 0
        self.views = 0


class VideoSharingPlatform:
    def __init__(self):
        self.video_library = {}  # key=id val=video_obj
        self.available_ids = []  # minHeap
        self.current_id_counter = 0

    def upload(self, video: str) -> int:
        if self.available_ids:
            curr_id = heappop(self.available_ids)
        else:
            curr_id = self.current_id_counter
            self.current_id_counter += 1

        self.video_library[curr_id] = Video(video)

        return curr_id

    def remove(self, videoId: int) -> None:
        if videoId not in self.video_library:
            return

        heappush(self.available_ids, videoId)
        self.video_library.pop(videoId)

    def watch(self, videoId: int, startMinute: int, endMinute: int) -> str:
        if videoId not in self.video_library:
            return '-1'

        vid = self.video_library[videoId]
        vid.views += 1

        return vid.content[startMinute: endMinute + 1]

    def like(self, videoId: int) -> None:
        if videoId in self.video_library:
            self.video_library[videoId].likes += 1

    def dislike(self, videoId: int) -> None:
        if videoId in self.video_library:
            self.video_library[videoId].dislikes += 1

    def getLikesAndDislikes(self, videoId: int) -> List[int]:
        if videoId not in self.video_library:
            return [-1]

        return [self.video_library[videoId].likes, self.video_library[videoId].dislikes]

    def getViews(self, videoId: int) -> int:
        if videoId not in self.video_library:
            return -1

        return self.video_library[videoId].views


# Your VideoSharingPlatform object will be instantiated and called as such:
# obj = VideoSharingPlatform()
# param_1 = obj.upload(video)
# obj.remove(videoId)
# param_3 = obj.watch(videoId,startMinute,endMinute)
# obj.like(videoId)
# obj.dislike(videoId)
# param_6 = obj.getLikesAndDislikes(videoId)
# param_7 = obj.getViews(videoId)
