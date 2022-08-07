import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song
from classes.cloak_room import CloakRoom


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.visiter_johnny = Guest("Johnny", 100, 1)
        self.visiter_brian = Guest("Brian", 100, 1)
        self.visiter_emma = Guest("Emma", 100, 1)
        self.visiter_sioban = Guest("Sioban", 100, 1)
        self.visiter_alex = Guest("Alex", 100, 1)
        self.visiter_sophie = Guest("Sophie", 100, 1)
        self.visiter_george = Guest("George", 100, 1)
        self.visiter_jimmy = Guest("Jimmy", 100, 1)
        self.visiter_sandra = Guest("Sandra", 100, 1)

        self.room_main = Room("Main", 5, 10, 0)
        self.room_upstairs = Room("Upstairs", 5, 10, 0)

        self.song_bon_jovi = Song("living On A Prayer")
        self.song_aerosmith = Song("Walk This Way!")
        self.song_beatles = Song("Help!")
        self.song_avicci = Song("Wake Me Up")
        self.coat_rack = CloakRoom(0, 1.50)


    
    def test_add_visiters_to_main_room(self):
        self.room_main.add_visiter_to_main_room(self.visiter_johnny, self.visiter_brian, self.visiter_emma, self.visiter_sioban, self.visiter_alex, self.visiter_sophie )
        self.visiter_johnny.money -= self.room_main.entry_fee
        self.room_main.till += self.room_main.entry_fee

        self.visiter_brian.money -= self.room_main.entry_fee
        self.room_main.till += self.room_main.entry_fee 

        self.visiter_emma.money -= self.room_main.entry_fee
        self.room_main.till += self.room_main.entry_fee 

        self.visiter_sioban.money -= self.room_main.vip_entry
        self.room_main.till += self.room_main.vip_entry 

        self.visiter_alex.money -= self.room_main.vip_entry
        self.room_main.till += self.room_main.vip_entry 

        self.visiter_sophie.money -= self.room_main.entry_fee
        self.room_main.till += self.room_main.entry_fee 

        self.assertEqual(self.visiter_johnny.money, 95)
        self.assertEqual(self.visiter_brian.money, 95)
        self.assertEqual(self.visiter_emma.money, 95)
        self.assertEqual(self.visiter_sophie.money, 95)
        self.assertEqual(self.visiter_sioban.money, 90)
        self.assertEqual(self.visiter_alex.money, 90)
        self.assertEqual(len(self.room_main.guest_list_main), 4)
        self.assertEqual(self.room_main.till, 40)


    def test_add_songs_to_main_room(self):
        self.room_main.add_song_to_main_room(self.song_bon_jovi, self.song_aerosmith)
        self.assertEqual(len(self.room_main.music_list_main), 2)
        

    def test_add_visiters_to_upstairs(self):
        self.room_upstairs.add_visiter_to_upstairs_room(self.visiter_george, self.visiter_jimmy, self.visiter_sandra)

        self.visiter_george.money -= self.room_upstairs.entry_fee
        self.room_upstairs.till += self.room_upstairs.entry_fee

        self.visiter_jimmy.money -= self.room_upstairs.vip_entry
        self.room_upstairs.till += self.room_upstairs.vip_entry

        self.visiter_sandra.money -= self.room_upstairs.entry_fee
        self.room_upstairs.till += self.room_upstairs.entry_fee

        self.assertEqual(self.visiter_george.money, 95)
        self.assertEqual(self.visiter_jimmy.money, 90)
        self.assertEqual(self.visiter_sandra.money, 95)
        self.assertEqual(len(self.room_upstairs.guest_list_upstairs), 2)
        self.assertEqual(self.room_upstairs.till, 20)

    def test_add_songs_to_upstairs(self):
        self.room_upstairs.add_song_to_upstairs_room(self.song_beatles, self.song_avicci)
        self.assertEqual(2, len(self.room_upstairs.music_list_upstairs))

    def test_guests_coats(self):
        self.coat_rack.coat_hanger += self.visiter_johnny.coat
        self.visiter_johnny.money -= self.coat_rack.coat_fee
        self.room_main.till += self.coat_rack.coat_fee

        self.coat_rack.coat_hanger += self.visiter_brian.coat
        self.visiter_brian.money -= self.coat_rack.coat_fee
        self.room_main.till += self.coat_rack.coat_fee

        self.coat_rack.coat_hanger += self.visiter_emma.coat
        self.visiter_emma.money -= self.coat_rack.coat_fee
        self.room_main.till += self.coat_rack.coat_fee

        self.coat_rack.coat_hanger += self.visiter_george.coat
        self.visiter_george.money -= self.coat_rack.coat_fee
        self.room_main.till += self.coat_rack.coat_fee

        self.coat_rack.coat_hanger += self.visiter_sandra.coat
        self.visiter_sandra.money -= self.coat_rack.coat_fee
        self.room_main.till += self.coat_rack.coat_fee

        

        self.assertEqual(5, self.coat_rack.coat_hanger)
        self.assertEqual(self.visiter_johnny.money, 98.50)
        self.assertEqual(self.visiter_brian.money, 98.50)
        self.assertEqual(self.visiter_emma.money, 98.50)
        self.assertEqual(self.visiter_george.money, 98.50)
        self.assertEqual(self.visiter_sandra.money, 98.50)
        self.assertEqual(self.room_main.till, 7.50)
        

        
    









