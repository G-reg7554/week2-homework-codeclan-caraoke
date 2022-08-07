class Room:
    def __init__(self, room_type, entry_fee, vip_entry):
        self.room = room_type
        self.entry_fee = entry_fee
        self.vip_entry = vip_entry
        self.guest_list_main = []
        self.guest_list_upstairs = []
        self.music_list_main = []
        self.music_list_upstairs = []

    def add_visiter_to_main_room(self, visiter, visiter1, visiter2, visiter3, visiter4, visiter5):
        self.guest_list_main.append(visiter)
        self.guest_list_main.append(visiter1)
        self.guest_list_main.append(visiter2)
        self.guest_list_main.append(visiter3)
        self.guest_list_main.append(visiter4)
        self.guest_list_main.append(visiter5)
        self.guest_list_main.remove(visiter)
        self.guest_list_main.remove(visiter3)

    def add_song_to_main_room(self, tunes, tunes1):
        self.music_list_main.append(tunes)
        self.music_list_main.append(tunes1)

    def add_visiter_to_upstairs_room(self, visiter6, visiter7, visiter8):
        self.guest_list_upstairs.append(visiter6)
        self.guest_list_upstairs.append(visiter7)
        self.guest_list_upstairs.append(visiter8)
        self.guest_list_upstairs.remove(visiter8)
    
    def add_song_to_upstairs_room(self, tunes3, tunes4):
        self.music_list_upstairs.append(tunes3)
        self.music_list_upstairs.append(tunes4)
