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
        self.room_main = Room(1)
        self.song_bon_jovi = Song("living on a prayer")

    
    def test_add_visiters_to_rooms(self):
        self.room_main.add_visiter_to_room(self.visiter_johnny, self.visiter_brian, self.visiter_emma, self.visiter_sioban, self.visiter_alex, self.visiter_sophie )
        self.assertEqual(len(self.room_main.guest_list), 4)

    def test_add_songs_to_rooms(self):
        self.room_main.add_song_to_room(self.song_bon_jovi)
        self.assertEqual(len(self.room_main.music_list), 1)

