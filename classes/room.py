class Room:
    def __init__(self, room_number):
        self.room = room_number
        self.guest_list = []
        self.music_list = []

    def add_visiter_to_room(self, visiter, visiter1, visiter2, visiter3, visiter4, visiter5):
        self.guest_list.append(visiter)
        self.guest_list.append(visiter1)
        self.guest_list.append(visiter2)
        self.guest_list.append(visiter3)
        self.guest_list.append(visiter4)
        self.guest_list.append(visiter5)
        self.guest_list.remove(visiter)
        self.guest_list.remove(visiter3)

    def add_song_to_room(self, tunes):
        self.music_list.append(tunes)