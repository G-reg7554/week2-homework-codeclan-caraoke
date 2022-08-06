import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.visiter_johnny = Guest("Johnny")
        self.visiter_brian = Guest("Brian")
        self.visiter_emma = Guest("Emma")
        self.visiter_sioban = Guest("Sioban")
        self.visiter_alex = Guest("Alex")
        self.visiter_sophie = Guest("Sophie")
        self.visiter_george = Guest("George")
        self.visiter_jimmy = Guest("Jimmy")
        self.visiter_sandra = Guest("Sandra")
        self.room_main = Room(1)
        self.room_upstairs = Room(2)
        self.song_bon_jovi = Song("living On A Prayer")
        self.song_aerosmith = Song("Walk This Way!")
        self.song_beatles = Song("Help!")
        self.song_avicci = Song("Wake Me Up")

    
    def test_add_visiters_to_main_room(self):
        self.room_main.add_visiter_to_main_room(self.visiter_johnny, self.visiter_brian, self.visiter_emma, self.visiter_sioban, self.visiter_alex, self.visiter_sophie )
        self.assertEqual(len(self.room_main.guest_list_main), 4)

    def test_add_songs_to_main_room(self):
        self.room_main.add_song_to_main_room(self.song_bon_jovi, self.song_aerosmith)
        self.assertEqual(len(self.room_main.music_list_main), 2)

    def test_add_visiters_to_upstairs(self):
        self.room_upstairs.add_visiter_to_upstairs_room(self.visiter_george, self.visiter_jimmy, self.visiter_sandra)
        self.assertEqual(len(self.room_upstairs.guest_list_upstairs), 2)

    def test_add_songs_to_upstairs(self):
        self.room_upstairs.add_song_to_upstairs_room(self.song_beatles, self.song_avicci)
        self.assertEqual(2, len(self.room_upstairs.music_list_upstairs))


