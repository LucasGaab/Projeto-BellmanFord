import networkx as nx
import matplotlib.pyplot as plt
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.nos = ['Akabanebashi', 'Azabu-Juban', 'Akabane-Iwabuchi', 'Shimo', 'Akasaka', 'Kokkai-gijidomae',
                    'Akasaka-Mitsuke', 'Tameike-Sanno', 'Akebonobashi', 'Ichigaya', 'Akihabara', 'Naka-Okachimachi',
                    'Aoyama-itchome', 'Asakusa', 'Tawaramachi', 'Asakusabashi', 'Kuramae', 'Awajicho', 'Ochanomizu',
                    'Ayase', 'Kita-Ayase', 'Roppongi-Itchome', 'Bakuroyokoyama', 'Higashi-Nihombashi',
                    'Baraki-Nakayama', 'Nishi-Funabashi', 'Chikatetsu-Akatsuka', 'Heiwadai', 'Chikatetsu-Narimasu',
                    'Daimon', 'Shimbashi', 'Ebisu', 'Hiro-o', 'Edogawabashi', 'Iidabashi', 'Funabori', 'Ichinoe',
                    'Gaiemmae', 'Ginza', 'Kyobashi', 'Ginza-itchome', 'Gokokuji', 'Gotanda', 'Takanawadai', 'Gyotoku',
                    'Myoden', 'Hakusan', 'Sengoku', 'Hamacho', 'Morishita', 'Hanzomon', 'Kudanshita', 'Hasune',
                    'Nishidai', 'Hatchobori', 'Kayabacho', 'Hikawadai', 'Hibiya', 'Higashi-Nakano', 'Nakai',
                    'Higashi-Ginza', 'Tsukiji', 'Higashi-Ikebukuro', 'Higashi-Koenji', 'Shin-Nakano', 'Higashi-Ojima',
                    'Higashi-Shinjuku', 'Shinjuku-sanchome', 'Hikarigaoka', 'Nerima-Kasugacho', 'Kotake-Mukaihara',
                    'Roppongi', 'Honancho', 'Nakano-Fujimicho', 'Hongo-sanchome', 'Korakuen', 'Honjo-Azumabashi',
                    'Oshiage', 'Hon-Komagome', 'Komagome', 'Kojimachi', 'Mizue', 'Ikebukuro', 'Shin-Otsuka', 'Inaricho',
                    'Iriya', 'Minowa', 'Itabashihoncho', 'Motohasunuma', 'Itabashi-Kuyakushomae', 'Iwamotocho',
                    'Jimbocho', 'Otemachi', 'Kachidoki',
                    'Tsukijishijo', 'Kagurazaka', 'Kamiyacho', 'Kasumigaseki', 'Kanamecho', 'Kanda', 'Suehirocho',
                    'Kasai', 'Urayasu', 'Kasuga', 'Ningyocho', 'Kiba', 'Toyocho', 'Kikukawa', 'Sumiyoshi', 'Kinshicho',
                    'Kita-sando', 'Meiji-Jingumae', 'Kita-Senju', 'Minami-Senju', 'Kiyosumi-shirakawa', 'Kodemmacho',
                    'Nagatacho', 'Kokuritsu-Kyogijo', 'Yoyogi', 'Nishigahara', 'Myogadani', 'Senkawa', 'Takebashi',
                    'Nihombashi', 'Machiya', 'Magome', 'Nakanobu', 'Meguro', 'Shirokanedai', 'Meiji-jingumae',
                    'Omote-sando', 'Minami-Asagaya', 'Shin-Koenji', 'Minami-Gyotoku', 'Minami-Sunamachi', 'Nishi-Kasai',
                    'Mita', 'Mitsukoshimae', 'Shinozaki', 'Monzen-Nakacho', 'Shimura-Sakaue', 'Motoyawata',
                    'Ochiai-Minami-Nagasaki', 'Naka-Meguro', 'Nakano', 'Ochiai', 'Togoshi', 'Nakano-Shimbashi',
                    'Nakano-Sakaue', 'Nishi-Shinjuku', 'Ueno', 'Nerima', 'Toshimaen', 'Nezu', 'Sendagi', 'Nijubashimae',
                    'Takashimadaira', 'Oji', 'Nishi-Magome', 'Nishi-Nippori', 'Nishi-Ojima', 'Ojima', 'Shinjuku',
                    'Nishi-Shinjuku-gochome', 'Nishi-Sugamo', 'Shin-Itabashi', 'Nishi-Takashimadaira',
                    'Shin-Takashimadaira', 'Nishi-Waseda', 'Nogizaka', 'Takadanobaba', 'Shin-Egota', 'Ogawamachi',
                    'Ogikubo', 'Oji-Kamiya', 'Onarimon', 'Uchisaiwaicho', 'Ryogoku', 'Sakuradamon', 'Yurakucho',
                    'Sengakuji', 'Sugamo', 'Shibakoen', 'Shibuya', 'Shimura-sanchome', 'Shinjuku-Gyoemmae',
                    'Yotsuya-sanchome', 'Shinjuku-Nishiguchi',
                    'Shin-Kiba', 'Tatsumi', 'Shin-Ochanomizu', 'Yushima', 'Shin-Okachimachi', 'Shintomicho',
                    'Tsukishima', 'Shiodome', 'Shirokane-Takanawa', 'Ueno-Hirokoji', 'Suidobashi', 'Suitengumae',
                    'Waseda', 'Takaracho', 'Toranomon', 'Tochomae', 'Todaimae', 'Tokyo', 'Toyosu', 'Ueno-Okachimachi',
                    'Ushigome-Kagurazaka', 'Ushigome-Yanagicho', 'Wakamatsu-Kawada', 'Wakoshi', 'Yotsuya',
                    'Yoyogi-koen', 'Yoyogi-Uehara', 'Zoshigaya', ]
        self.grafo = [['Akabanebashi', 'Azabu-Juban', 0.8], ['Akabane-Iwabuchi', 'Shimo', 1.1],
                      ['Akasaka', 'Kokkai-gijidomae', 0.8], ['Akasaka-Mitsuke', 'Tameike-Sanno', 0.9],
                      ['Akebonobashi', 'Ichigaya', 1.4], ['Akihabara', 'Naka-Okachimachi', 1.0],
                      ['Aoyama-itchome', 'Akasaka-Mitsuke', 1.3], ['Asakusa', 'Tawaramachi', 0.8],
                      ['Asakusabashi', 'Kuramae', 0.7], ['Awajicho', 'Ochanomizu', 0.8], ['Ayase', 'Kita-Ayase', 2.1],
                      ['Azabu-Juban', 'Roppongi-Itchome', 1.2], ['Bakuroyokoyama', 'Higashi-Nihombashi', 0.0],
                      ['Baraki-Nakayama', 'Nishi-Funabashi', 1.9], ['Chikatetsu-Akatsuka', 'Heiwadai', 1.8],
                      ['Chikatetsu-Narimasu', 'Chikatetsu-Akatsuka', 1.4], ['Daimon', 'Shimbashi', 1.0],
                      ['Ebisu', 'Hiro-o', 1.5], ['Edogawabashi', 'Iidabashi', 1.6], ['Funabori', 'Ichinoe', 1.7],
                      ['Gaiemmae', 'Aoyama-itchome', 0.7], ['Ginza', 'Kyobashi', 0.7], ['Ginza-itchome', 'Ginza', 0.0],
                      ['Gokokuji', 'Edogawabashi', 1.3], ['Gotanda', 'Takanawadai', 1.3], ['Gyotoku', 'Myoden', 1.3],
                      ['Hakusan', 'Sengoku', 1.0], ['Hamacho', 'Morishita', 0.8], ['Hanzomon', 'Kudanshita', 1.6],
                      ['Hasune', 'Nishidai', 0.8], ['Hatchobori', 'Kayabacho', 0.5], ['Heiwadai', 'Hikawadai', 1.4],
                      ['Hibiya', 'Ginza', 0.4], ['Higashi-Nakano', 'Nakai', 0.8], ['Higashi-Ginza', 'Tsukiji', 0.6],
                      ['Higashi-Ikebukuro', 'Gokokuji', 1.1], ['Higashi-Koenji', 'Shin-Nakano', 1.0],
                      ['Higashi-Nihombashi', 'Asakusabashi', 0.7], ['Higashi-Ojima', 'Funabori', 1.7],
                      ['Higashi-Shinjuku', 'Shinjuku-sanchome', 1.1], ['Hikarigaoka', 'Nerima-Kasugacho', 1.4],
                      ['Hikawadai', 'Kotake-Mukaihara', 1.5], ['Hiro-o', 'Roppongi', 1.7],
                      ['Honancho', 'Nakano-Fujimicho', 1.3], ['Hongo-sanchome', 'Korakuen', 0.8],
                      ['Honjo-Azumabashi', 'Oshiage', 0.8], ['Hon-Komagome', 'Komagome', 1.4],
                      ['Ichigaya', 'Kojimachi', 0.9], ['Ichinoe', 'Mizue', 1.7], ['Iidabashi', 'Kudanshita', 0.7],
                      ['Ikebukuro', 'Shin-Otsuka', 1.8], ['Inaricho', 'Tawaramachi', 0.7], ['Iriya', 'Minowa', 1.2],
                      ['Itabashihoncho', 'Motohasunuma', 0.9], ['Itabashi-Kuyakushomae', 'Itabashihoncho', 1.2],
                      ['Iwamotocho', 'Akihabara', 0.0], ['Jimbocho', 'Otemachi', 1.7],
                      ['Kachidoki', 'Tsukijishijo', 1.5], ['Kagurazaka', 'Iidabashi', 1.2],
                      ['Kamiyacho', 'Kasumigaseki', 1.3], ['Kanamecho', 'Ikebukuro', 1.2], ['Kanda', 'Suehirocho', 1.1],
                      ['Kasai', 'Urayasu', 1.9], ['Kasuga', 'Korakuen', 0.0], ['Kasumigaseki', 'Ginza', 1.0],
                      ['Kayabacho', 'Ningyocho', 0.9], ['Kiba', 'Toyocho', 0.9], ['Kikukawa', 'Sumiyoshi', 0.9],
                      ['Kinshicho', 'Oshiage', 1.4], ['Kita-Ayase', 'Ayase', 2.1],
                      ['Kita-sando', 'Meiji-Jingumae', 1.2], ['Kita-Senju', 'Minami-Senju', 2.1],
                      ['Kiyosumi-shirakawa', 'Sumiyoshi', 1.9], ['Kodemmacho', 'Akihabara', 0.9],
                      ['Kojimachi', 'Nagatacho', 0.9], ['Kokkai-gijidomae', 'Tameike-Sanno', 0.0],
                      ['Kokuritsu-Kyogijo', 'Yoyogi', 1.5], ['Komagome', 'Nishigahara', 1.4],
                      ['Korakuen', 'Myogadani', 1.8], ['Kotake-Mukaihara', 'Senkawa', 1.0],
                      ['Kudanshita', 'Takebashi', 1.0], ['Kuramae', 'Asakusa', 0.9], ['Kyobashi', 'Nihombashi', 0.7],
                      ['Machiya', 'Kita-Senju', 2.6], ['Magome', 'Nakanobu', 0.9], ['Meguro', 'Shirokanedai', 1.3],
                      ['Meiji-jingumae', 'Omote-sando', 0.9], ['Minami-Asagaya', 'Shin-Koenji', 1.2],
                      ['Minami-Gyotoku', 'Gyotoku', 1.5], ['Minami-Senju', 'Kita-Senju', 2.1],
                      ['Minami-Sunamachi', 'Nishi-Kasai', 2.7], ['Minowa', 'Minami-Senju', 0.8],
                      ['Mita', 'Daimon', 1.5], ['Mitsukoshimae', 'Kanda', 0.7], ['Mizue', 'Shinozaki', 1.5],
                      ['Monzen-Nakacho', 'Kiba', 1.1], ['Morishita', 'Kikukawa', 0.8],
                      ['Motohasunuma', 'Shimura-Sakaue', 1.1], ['Motoyawata', 'Shinozaki', 2.8],
                      ['Myoden', 'Baraki-Nakayama', 2.1], ['Myogadani', 'Shin-Otsuka', 1.2],
                      ['Nagatacho', 'Akasaka-Mitsuke', 0.0], ['Nakai', 'Ochiai-Minami-Nagasaki', 1.3],
                      ['Naka-Meguro', 'Ebisu', 1.0], ['Nakano', 'Ochiai', 2.0], ['Nakanobu', 'Togoshi', 1.1],
                      ['Nakano-Fujimicho', 'Nakano-Shimbashi', 0.6], ['Nakano-Sakaue', 'Nishi-Shinjuku', 1.1],
                      ['Nakano-Shimbashi', 'Nakano-Sakaue', 1.3], ['Naka-Okachimachi', 'Ueno', 0.5],
                      ['Nerima', 'Toshimaen', 0.9], ['Nerima-Kasugacho', 'Hikarigaoka', 1.4], ['Nezu', 'Sendagi', 1.0],
                      ['Nihombashi', 'Mitsukoshimae', 0.6], ['Nijubashimae', 'Otemachi', 0.7],
                      ['Ningyocho', 'Kodemmacho', 0.6], ['Nishidai', 'Takashimadaira', 1.0],
                      ['Nishi-Funabashi', 'Baraki-Nakayama', 1.9], ['Nishigahara', 'Oji', 1.0],
                      ['Nishi-Kasai', 'Kasai', 1.2], ['Nishi-Magome', 'Magome', 1.2], ['Nishi-Nippori', 'Machiya', 1.7],
                      ['Nishi-Ojima', 'Ojima', 0.7], ['Nishi-Shinjuku', 'Shinjuku', 0.8],
                      ['Nishi-Shinjuku-gochome', 'Nakano-Sakaue', 1.2], ['Nishi-Sugamo', 'Shin-Itabashi', 1.0],
                      ['Nishi-Takashimadaira', 'Shin-Takashimadaira', 0.8], ['Nishi-Waseda', 'Higashi-Shinjuku', 0.9],
                      ['Nogizaka', 'Akasaka', 1.1], ['Ochanomizu', 'Hongo-sanchome', 0.8],
                      ['Ochiai', 'Takadanobaba', 1.9], ['Ochiai-Minami-Nagasaki', 'Shin-Egota', 1.6],
                      ['Ogawamachi', 'Awajicho', 0.0], ['Ogikubo', 'Minami-Asagaya', 1.5], ['Oji', 'Oji-Kamiya', 1.2],
                      ['Oji-Kamiya', 'Shimo', 1.6], ['Ojima', 'Higashi-Ojima', 1.2], ['Omote-sando', 'Gaiemmae', 0.7],
                      ['Onarimon', 'Uchisaiwaicho', 1.1], ['Oshiage', 'Kinshicho', 1.4], ['Otemachi', 'Awajicho', 0.9],
                      ['Roppongi', 'Kamiyacho', 1.5], ['Roppongi-Itchome', 'Tameike-Sanno', 0.9],
                      ['Ryogoku', 'Morishita', 1.0], ['Sakuradamon', 'Yurakucho', 1.0],
                      ['Sendagi', 'Nishi-Nippori', 0.9], ['Sengakuji', 'Mita', 1.1], ['Sengoku', 'Sugamo', 0.9],
                      ['Senkawa', 'Kanamecho', 1.0], ['Shibakoen', 'Onarimon', 0.7], ['Shibuya', 'Omote-sando', 1.3],
                      ['Shimbashi', 'Ginza', 0.9], ['Shimo', 'Akabane-Iwabuchi', 1.1],
                      ['Shimura-Sakaue', 'Shimura-sanchome', 0.9], ['Shimura-sanchome', 'Hasune', 1.2],
                      ['Shin-Egota', 'Nerima', 1.6], ['Shin-Itabashi', 'Itabashi-Kuyakushomae', 0.9],
                      ['Shinjuku', 'Shinjuku-sanchome', 0.3], ['Shinjuku-Gyoemmae', 'Yotsuya-sanchome', 0.9],
                      ['Shinjuku-Nishiguchi', 'Shinjuku', 0.0], ['Shinjuku-sanchome', 'Shinjuku-Gyoemmae', 0.7],
                      ['Shin-Kiba', 'Tatsumi', 1.5], ['Shin-Koenji', 'Higashi-Koenji', 0.9],
                      ['Shin-Nakano', 'Nakano-Sakaue', 1.1], ['Shin-Ochanomizu', 'Yushima', 1.2],
                      ['Shin-Okachimachi', 'Kuramae', 1.0], ['Shin-Otsuka', 'Ikebukuro', 1.8],
                      ['Shinozaki', 'Motoyawata', 2.8], ['Shin-Takashimadaira', 'Nishi-Takashimadaira', 0.8],
                      ['Shintomicho', 'Tsukishima', 1.3], ['Shiodome', 'Daimon', 0.9],
                      ['Shirokanedai', 'Shirokane-Takanawa', 1.0], ['Shirokane-Takanawa', 'Azabu-Juban', 1.3],
                      ['Suehirocho', 'Ueno-Hirokoji', 0.6], ['Sugamo', 'Nishi-Sugamo', 1.4],
                      ['Suidobashi', 'Kasuga', 0.7], ['Suitengumae', 'Kiyosumi-shirakawa', 1.7],
                      ['Sumiyoshi', 'Kinshicho', 1.0], ['Takadanobaba', 'Waseda', 1.7],
                      ['Takanawadai', 'Sengakuji', 1.4], ['Takaracho', 'Nihombashi', 0.8],
                      ['Takashimadaira', 'Shin-Takashimadaira', 0.7], ['Takebashi', 'Otemachi', 1.0],
                      ['Tameike-Sanno', 'Toranomon', 0.6], ['Tatsumi', 'Shin-Kiba', 1.5],
                      ['Tawaramachi', 'Asakusa', 0.8], ['Tochomae', 'Nishi-Shinjuku-gochome', 0.8],
                      ['Todaimae', 'Hon-Komagome', 0.9], ['Togoshi', 'Gotanda', 1.0], ['Tokyo', 'Otemachi', 0.6],
                      ['Toranomon', 'Shimbashi', 0.8], ['Toshimaen', 'Nerima-Kasugacho', 1.5],
                      ['Toyocho', 'Minami-Sunamachi', 1.2], ['Toyosu', 'Tatsumi', 1.7], ['Tsukiji', 'Hatchobori', 1.0],
                      ['Tsukijishijo', 'Shiodome', 0.9], ['Tsukishima', 'Toyosu', 1.4],
                      ['Uchisaiwaicho', 'Hibiya', 0.9], ['Ueno', 'Inaricho', 0.7], ['Ueno-Hirokoji', 'Ueno', 0.5],
                      ['Ueno-Okachimachi', 'Ueno-Hirokoji', 0.0], ['Urayasu', 'Minami-Gyotoku', 1.2],
                      ['Ushigome-Kagurazaka', 'Iidabashi', 1.0], ['Ushigome-Yanagicho', 'Ushigome-Kagurazaka', 1.0],
                      ['Wakamatsu-Kawada', 'Ushigome-Yanagicho', 0.6], ['Wakoshi', 'Chikatetsu-Narimasu', 2.2],
                      ['Waseda', 'Kagurazaka', 1.2], ['Yotsuya', 'Akasaka-Mitsuke', 1.3],
                      ['Yotsuya-sanchome', 'Yotsuya', 1.0], ['Yoyogi', 'Shinjuku', 0.6],
                      ['Yoyogi-koen', 'Meiji-jingumae', 1.2], ['Yoyogi-Uehara', 'Yoyogi-koen', 1.0],
                      ['Yurakucho', 'Hibiya', 0.0], ['Yushima', 'Nezu', 1.2], ['Zoshigaya', 'Nishi-Waseda', 1.5],
                      ['Akabanebashi', 'Daimon', 1.3], ['Akasaka', 'Nogizaka', 1.1],
                      ['Akasaka-Mitsuke', 'Aoyama-itchome', 1.3], ['Akebonobashi', 'Shinjuku-sanchome', 1.5],
                      ['Akihabara', 'Kodemmacho', 0.9], ['Aoyama-itchome', 'Gaiemmae', 0.7],
                      ['Asakusa', 'Honjo-Azumabashi', 0.7], ['Asakusabashi', 'Higashi-Nihombashi', 0.7],
                      ['Awajicho', 'Otemachi', 0.9], ['Ayase', 'Kita-Senju', 2.6],
                      ['Azabu-Juban', 'Shirokane-Takanawa', 1.3], ['Bakuroyokoyama', 'Hamacho', 0.6],
                      ['Baraki-Nakayama', 'Myoden', 2.1], ['Chikatetsu-Akatsuka', 'Chikatetsu-Narimasu', 1.4],
                      ['Chikatetsu-Narimasu', 'Wakoshi', 2.2], ['Daimon', 'Mita', 1.5], ['Ebisu', 'Naka-Meguro', 1.0],
                      ['Edogawabashi', 'Gokokuji', 1.3], ['Funabori', 'Higashi-Ojima', 1.7],
                      ['Gaiemmae', 'Omote-sando', 0.7], ['Ginza', 'Shimbashi', 0.9],
                      ['Ginza-itchome', 'Shintomicho', 0.7], ['Gokokuji', 'Higashi-Ikebukuro', 1.1],
                      ['Gotanda', 'Togoshi', 1.0], ['Gyotoku', 'Minami-Gyotoku', 1.5], ['Hakusan', 'Kasuga', 1.4],
                      ['Hamacho', 'Bakuroyokoyama', 0.6], ['Hanzomon', 'Nagatacho', 1.0],
                      ['Hasune', 'Shimura-sanchome', 1.2], ['Hatchobori', 'Tsukiji', 1.0],
                      ['Heiwadai', 'Chikatetsu-Akatsuka', 1.8], ['Hibiya', 'Kasumigaseki', 1.2],
                      ['Higashi-Nakano', 'Nakano-Sakaue', 1.0], ['Higashi-Ginza', 'Ginza', 0.4],
                      ['Higashi-Ikebukuro', 'Ikebukuro', 0.9], ['Higashi-Koenji', 'Shin-Koenji', 0.9],
                      ['Higashi-Nihombashi', 'Ningyocho', 0.8], ['Higashi-Ojima', 'Ojima', 1.2],
                      ['Higashi-Shinjuku', 'Nishi-Waseda', 0.9], ['Hikawadai', 'Heiwadai', 1.4],
                      ['Hiro-o', 'Ebisu', 1.5], ['Hongo-sanchome', 'Ochanomizu', 0.8],
                      ['Honjo-Azumabashi', 'Asakusa', 0.7], ['Hon-Komagome', 'Todaimae', 0.9],
                      ['Ichigaya', 'Iidabashi', 1.1], ['Ichinoe', 'Funabori', 1.7], ['Iidabashi', 'Kagurazaka', 1.2],
                      ['Ikebukuro', 'Higashi-Ikebukuro', 0.9], ['Inaricho', 'Ueno', 0.7], ['Iriya', 'Ueno', 1.2],
                      ['Itabashihoncho', 'Itabashi-Kuyakushomae', 1.2], ['Itabashi-Kuyakushomae', 'Shin-Itabashi', 0.9],
                      ['Iwamotocho', 'Bakuroyokoyama', 0.8], ['Jimbocho', 'Kudanshita', 0.4],
                      ['Kachidoki', 'Tsukishima', 0.8], ['Kagurazaka', 'Waseda', 1.2], ['Kamiyacho', 'Roppongi', 1.5],
                      ['Kanamecho', 'Senkawa', 1.0], ['Kanda', 'Mitsukoshimae', 0.7], ['Kasai', 'Nishi-Kasai', 1.2],
                      ['Kasuga', 'Hakusan', 1.4], ['Kasumigaseki', 'Kokkai-gijidomae', 0.7],
                      ['Kayabacho', 'Hatchobori', 0.5], ['Kiba', 'Monzen-Nakacho', 1.1], ['Kikukawa', 'Morishita', 0.8],
                      ['Kinshicho', 'Sumiyoshi', 1.0], ['Kita-sando', 'Shinjuku-sanchome', 1.4],
                      ['Kita-Senju', 'Ayase', 2.6], ['Kiyosumi-shirakawa', 'Suitengumae', 1.7],
                      ['Kodemmacho', 'Ningyocho', 0.6], ['Kojimachi', 'Ichigaya', 0.9],
                      ['Kokkai-gijidomae', 'Kasumigaseki', 0.7], ['Kokuritsu-Kyogijo', 'Aoyama-itchome', 1.2],
                      ['Komagome', 'Hon-Komagome', 1.4], ['Korakuen', 'Hongo-sanchome', 0.8],
                      ['Kotake-Mukaihara', 'Hikawadai', 1.5], ['Kudanshita', 'Iidabashi', 0.7],
                      ['Kuramae', 'Asakusabashi', 0.7], ['Kyobashi', 'Ginza', 0.7], ['Machiya', 'Nishi-Nippori', 1.7],
                      ['Magome', 'Nishi-Magome', 1.2], ['Meguro', 'Shirokanedai', 1.3],
                      ['Meiji-jingumae', 'Yoyogi-koen', 1.2], ['Minami-Asagaya', 'Ogikubo', 1.5],
                      ['Minami-Gyotoku', 'Urayasu', 1.2], ['Minami-Senju', 'Minowa', 0.8],
                      ['Minami-Sunamachi', 'Toyocho', 1.2], ['Minowa', 'Iriya', 1.2], ['Mita', 'Sengakuji', 1.1],
                      ['Mitsukoshimae', 'Nihombashi', 0.6], ['Mizue', 'Ichinoe', 1.7],
                      ['Monzen-Nakacho', 'Kayabacho', 1.8], ['Morishita', 'Hamacho', 0.8],
                      ['Motohasunuma', 'Itabashihoncho', 0.9], ['Myoden', 'Gyotoku', 1.3],
                      ['Myogadani', 'Korakuen', 1.8], ['Nagatacho', 'Sakuradamon', 0.9],
                      ['Nakai', 'Higashi-Nakano', 0.8], ['Nakanobu', 'Magome', 0.9],
                      ['Nakano-Fujimicho', 'Honancho', 1.3], ['Nakano-Sakaue', 'Shin-Nakano', 1.1],
                      ['Nakano-Shimbashi', 'Nakano-Fujimicho', 0.6], ['Naka-Okachimachi', 'Akihabara', 1.0],
                      ['Nerima', 'Shin-Egota', 1.6], ['Nerima-Kasugacho', 'Toshimaen', 1.5], ['Nezu', 'Yushima', 1.2],
                      ['Nihombashi', 'Kyobashi', 0.7], ['Nijubashimae', 'Hibiya', 0.7], ['Ningyocho', 'Kayabacho', 0.9],
                      ['Nishidai', 'Hasune', 0.8], ['Nishigahara', 'Komagome', 1.4],
                      ['Nishi-Kasai', 'Minami-Sunamachi', 2.7], ['Nishi-Nippori', 'Sendagi', 0.9],
                      ['Nishi-Ojima', 'Sumiyoshi', 1.0], ['Nishi-Shinjuku', 'Nakano-Sakaue', 1.1],
                      ['Nishi-Shinjuku-gochome', 'Tochomae', 0.8], ['Nishi-Sugamo', 'Sugamo', 1.4],
                      ['Nishi-Waseda', 'Zoshigaya', 1.5], ['Nogizaka', 'Omote-sando', 1.4],
                      ['Ochanomizu', 'Awajicho', 0.8], ['Ochiai', 'Nakano', 2.0],
                      ['Ochiai-Minami-Nagasaki', 'Nakai', 1.3], ['Ogawamachi', 'Shin-Ochanomizu', 0.0],
                      ['Oji', 'Nishigahara', 1.0], ['Oji-Kamiya', 'Oji', 1.2], ['Ojima', 'Nishi-Ojima', 0.7],
                      ['Omote-sando', 'Shibuya', 1.3], ['Onarimon', 'Shibakoen', 0.7],
                      ['Oshiage', 'Honjo-Azumabashi', 0.8], ['Otemachi', 'Tokyo', 0.6], ['Roppongi', 'Hiro-o', 1.7],
                      ['Roppongi-Itchome', 'Azabu-Juban', 1.2], ['Ryogoku', 'Kuramae', 1.2],
                      ['Sakuradamon', 'Nagatacho', 0.9], ['Sendagi', 'Nezu', 1.0], ['Sengakuji', 'Takanawadai', 1.4],
                      ['Sengoku', 'Hakusan', 1.0], ['Senkawa', 'Kotake-Mukaihara', 1.0], ['Shibakoen', 'Mita', 0.6],
                      ['Shibuya', 'Omote-sando', 1.3], ['Shimbashi', 'Toranomon', 0.8], ['Shimo', 'Oji-Kamiya', 1.6],
                      ['Shimura-Sakaue', 'Motohasunuma', 1.1], ['Shimura-sanchome', 'Shimura-Sakaue', 0.9],
                      ['Shin-Egota', 'Ochiai-Minami-Nagasaki', 1.6], ['Shin-Itabashi', 'Nishi-Sugamo', 1.0],
                      ['Shinjuku', 'Nishi-Shinjuku', 0.8], ['Shinjuku-Gyoemmae', 'Shinjuku-sanchome', 0.7],
                      ['Shinjuku-Nishiguchi', 'Higashi-Shinjuku', 1.4], ['Shinjuku-sanchome', 'Shinjuku', 0.3],
                      ['Shin-Koenji', 'Minami-Asagaya', 1.2], ['Shin-Nakano', 'Higashi-Koenji', 1.0],
                      ['Shin-Ochanomizu', 'Otemachi', 1.3], ['Shin-Okachimachi', 'Ueno-Okachimachi', 0.8],
                      ['Shin-Otsuka', 'Myogadani', 1.2], ['Shinozaki', 'Mizue', 1.5],
                      ['Shin-Takashimadaira', 'Takashimadaira', 0.7], ['Shintomicho', 'Ginza-itchome', 0.7],
                      ['Shiodome', 'Tsukijishijo', 0.9], ['Shirokanedai', 'Meguro', 1.3],
                      ['Shirokane-Takanawa', 'Shirokanedai', 1.0], ['Suehirocho', 'Kanda', 1.1],
                      ['Sugamo', 'Sengoku', 0.9], ['Suidobashi', 'Jimbocho', 1.0],
                      ['Suitengumae', 'Mitsukoshimae', 1.3], ['Sumiyoshi', 'Kiyosumi-shirakawa', 1.9],
                      ['Takadanobaba', 'Ochiai', 1.9], ['Takanawadai', 'Gotanda', 1.3],
                      ['Takaracho', 'Higashi-Ginza', 0.8], ['Takashimadaira', 'Nishidai', 1.0],
                      ['Takebashi', 'Kudanshita', 1.0], ['Tameike-Sanno', 'Akasaka-Mitsuke', 0.9],
                      ['Tatsumi', 'Toyosu', 1.7], ['Tawaramachi', 'Inaricho', 0.7], ['Tochomae', 'Shinjuku', 0.8],
                      ['Todaimae', 'Korakuen', 1.3], ['Togoshi', 'Nakanobu', 1.1], ['Tokyo', 'Ginza', 1.1],
                      ['Toranomon', 'Tameike-Sanno', 0.6], ['Toshimaen', 'Nerima', 0.9], ['Toyocho', 'Kiba', 0.9],
                      ['Toyosu', 'Tsukishima', 1.4], ['Tsukiji', 'Higashi-Ginza', 0.6],
                      ['Tsukijishijo', 'Kachidoki', 1.5], ['Tsukishima', 'Shintomicho', 1.3],
                      ['Uchisaiwaicho', 'Onarimon', 1.1], ['Ueno', 'Ueno-Hirokoji', 0.5],
                      ['Ueno-Hirokoji', 'Suehirocho', 0.6], ['Ueno-Okachimachi', 'Naka-Okachimachi', 0.0],
                      ['Urayasu', 'Kasai', 1.9], ['Ushigome-Kagurazaka', 'Ushigome-Yanagicho', 1.0],
                      ['Ushigome-Yanagicho', 'Wakamatsu-Kawada', 0.6], ['Wakamatsu-Kawada', 'Higashi-Shinjuku', 1.0],
                      ['Wakoshi', 'Chikatetsu-Narimasu', 2.2], ['Waseda', 'Takadanobaba', 1.7],
                      ['Yotsuya', 'Yotsuya-sanchome', 1.0], ['Yotsuya-sanchome', 'Shinjuku-Gyoemmae', 0.9],
                      ['Yoyogi', 'Kokuritsu-Kyogijo', 1.5], ['Yoyogi-koen', 'Yoyogi-Uehara', 1.0],
                      ['Yurakucho', 'Ginza-itchome', 0.5], ['Yushima', 'Shin-Ochanomizu', 1.2],
                      ['Zoshigaya', 'Ikebukuro', 1.8], ['Akasaka-Mitsuke', 'Nagatacho', 0.0],
                      ['Akihabara', 'Iwamotocho', 0.0], ['Aoyama-itchome', 'Nagatacho', 1.4],
                      ['Asakusa', 'Kuramae', 0.9], ['Awajicho', 'Shin-Ochanomizu', 0.0],
                      ['Azabu-Juban', 'Roppongi', 1.1], ['Bakuroyokoyama', 'Iwamotocho', 0.8],
                      ['Chikatetsu-Akatsuka', 'Heiwadai', 1.8], ['Chikatetsu-Narimasu', 'Chikatetsu-Akatsuka', 1.4],
                      ['Daimon', 'Akabanebashi', 1.3], ['Ginza', 'Ginza-itchome', 0.0],
                      ['Ginza-itchome', 'Yurakucho', 0.5], ['Heiwadai', 'Hikawadai', 1.4], ['Hibiya', 'Yurakucho', 0.0],
                      ['Higashi-Ginza', 'Takaracho', 0.8], ['Higashi-Nihombashi', 'Bakuroyokoyama', 0.0],
                      ['Higashi-Shinjuku', 'Wakamatsu-Kawada', 1.0], ['Hikawadai', 'Kotake-Mukaihara', 1.5],
                      ['Hongo-sanchome', 'Ueno-Okachimachi', 1.1], ['Ichigaya', 'Iidabashi', 1.1],
                      ['Iidabashi', 'Ichigaya', 1.1], ['Ikebukuro', 'Kanamecho', 1.2],
                      ['Iwamotocho', 'Ogawamachi', 0.8], ['Jimbocho', 'Suidobashi', 1.0],
                      ['Kanamecho', 'Ikebukuro', 0.9], ['Kasuga', 'Suidobashi', 0.7], ['Kasumigaseki', 'Hibiya', 1.2],
                      ['Kayabacho', 'Monzen-Nakacho', 1.8], ['Kita-Senju', 'Machiya', 2.6],
                      ['Kiyosumi-shirakawa', 'Monzen-Nakacho', 1.2], ['Kokkai-gijidomae', 'Akasaka-Mitsuke', 0.9],
                      ['Korakuen', 'Kasuga', 0.0], ['Kotake-Mukaihara', 'Senkawa', 1.1],
                      ['Kudanshita', 'Jimbocho', 0.4], ['Kuramae', 'Ryogoku', 1.2], ['Meiji-jingumae', 'Shibuya', 1.0],
                      ['Mita', 'Shibakoen', 0.6], ['Mitsukoshimae', 'Suitengumae', 1.3],
                      ['Monzen-Nakacho', 'Tsukishima', 1.4], ['Morishita', 'Kiyosumi-shirakawa', 0.6],
                      ['Nagatacho', 'Kojimachi', 0.9], ['Nakano-Sakaue', 'Nakano-Shimbashi', 1.3],
                      ['Naka-Okachimachi', ' Ueno-Hirokoji', 0.0], ['Nihombashi', 'Kayabacho', 0.5],
                      ['Ningyocho', 'Suitengumae', 0.0], ['Ogawamachi', 'Iwamotocho', 0.8],
                      ['Omote-sando', 'Nogizaka', 1.4], ['Otemachi', 'Nihombashi', 0.8],
                      ['Roppongi', 'Aoyama-itchome', 1.3], ['Senkawa', 'Kanamecho', 1.0],
                      ['Shibuya', 'Meiji-Jingumae', 1.0], ['Shimbashi', 'Higashi-Ginza', 0.9],
                      ['Shinjuku', 'Shinjuku-Nishiguchi', 0.0], ['Shinjuku-Nishiguchi', 'Tochomae', 0.8],
                      ['Shinjuku-sanchome', 'Kita-sando', 1.4], ['Shin-Ochanomizu', 'Awajicho', 0.0],
                      ['Shintomicho', 'Tsukiji', 0.0], ['Shirokanedai', 'Shirokane-Takanawa', 1.0],
                      ['Shirokane-Takanawa', 'Mita', 1.7], ['Suitengumae', 'Ningyocho', 0.0],
                      ['Sumiyoshi', 'Nishi-Ojima', 1.0], ['Tameike-Sanno', 'Kokkai-gijidomae', 0.0],
                      ['Tochomae', 'Shinjuku-Nishiguchi', 0.8], ['Tsukiji', 'Shintomicho', 0.0],
                      ['Tsukishima', 'Kachidoki', 0.8], ['Ueno', 'Iriya', 1.2],
                      ['Ueno-Hirokoji', 'Naka-Okachimachi', 0.0], ['Ueno-Okachimachi', 'Shin-Okachimachi', 0.8],
                      ['Yotsuya', 'Ichigaya', 1.0], ['Yurakucho', 'Sakuradamon', 1.0],
                      ['Akasaka-Mitsuke', 'Kokkai-gijidomae', 0.9], ['Aoyama-itchome', 'Omote-sando', 1.4],
                      ['Awajicho', 'Ogawamachi', 0.0], ['Azabu-Juban', 'Akabanebashi', 0.8],
                      ['Chikatetsu-Akatsuka', 'Chikatetsu-Narimasu', 1.4], ['Chikatetsu-Narimasu', 'Wakoshi', 2.2],
                      ['Daimon', 'Shiodome', 0.9], ['Ginza', 'Tokyo', 1.1], ['Heiwadai', 'Chikatetsu-Akatsuka', 1.8],
                      ['Hibiya', 'Nijubashimae', 0.7], ['Higashi-Ginza', 'Shimbashi', 0.9],
                      ['Higashi-Shinjuku', 'Shinjuku-Nishiguchi', 1.4], ['Hikawadai', 'Heiwadai', 1.4],
                      ['Hongo-sanchome', 'Kasuga', 0.8], ['Ichigaya', 'Yotsuya', 1.0],
                      ['Iidabashi', 'Edogawabashi', 1.6], ['Ikebukuro', 'Zoshigaya', 1.8],
                      ['Jimbocho', 'Otemachi', 1.4], ['Kanamecho', 'Senkawa', 1.0], ['Kasuga', 'Hongo-sanchome', 0.8],
                      ['Kasumigaseki', 'Kamiyacho', 1.3], ['Kayabacho', 'Nihombashi', 0.5],
                      ['Kiyosumi-shirakawa', 'Morishita', 0.6], ['Kokkai-gijidomae', 'Kasumigaseki', 0.8],
                      ['Korakuen', 'Todaimae', 1.3], ['Kotake-Mukaihara', 'Hikawadai', 1.5],
                      ['Kudanshita', 'Hanzomon', 1.6], ['Kuramae', 'Shin-Okachimachi', 1.0],
                      ['Meiji-jingumae', 'Kita-sando', 1.2], ['Mita', 'Shirokane-Takanawa', 1.7],
                      ['Mitsukoshimae', 'Otemachi', 0.7], ['Monzen-Nakacho', 'Kiyosumi-shirakawa', 1.2],
                      ['Morishita', 'Ryogoku', 1.0], ['Nagatacho', 'Hanzomon', 1.0],
                      ['Nakano-Sakaue', 'Higashi-Nakano', 1.0], ['Naka-Okachimachi', 'Ueno-Okachimachi', 0.0],
                      ['Nihombashi', 'Otemachi', 0.8], ['Ningyocho', 'Higashi-Nihombashi', 0.8],
                      ['Ogawamachi', 'Jimbocho', 0.9], ['Omote-sando', 'Meiji-jingumae', 0.9],
                      ['Otemachi', 'Takebashi', 1.0], ['Roppongi', 'Azabu-Juban', 1.1],
                      ['Senkawa', 'Kotake-Mukaihara', 1.1], ['Shimbashi', 'Daimon', 1.0],
                      ['Shinjuku', 'Shinjuku-sanchome', 0.8], ['Shinjuku-sanchome', 'Higashi-Shinjuku', 1.1],
                      ['Shin-Ochanomizu', 'Ogawamachi', 0.0], ['Shirokanedai', 'Meguro', 1.3],
                      ['Shirokane-Takanawa', 'Shirokanedai', 1.0], ['Sumiyoshi', 'Kikukawa', 0.9],
                      ['Tameike-Sanno', 'Nagatacho', 0.9], ['Tsukishima', 'Monzen-Nakacho', 1.4],
                      ['Ueno', 'Naka-Okachimachi', 0.5], ['Ueno-Hirokoji', 'Ueno-Okachimachi', 0.0],
                      ['Ueno-Okachimachi', 'Hongo-sanchome', 1.1], ['Yotsuya', 'Nagatacho', 1.3],
                      ['Akasaka-Mitsuke', 'Yotsuya', 1.3], ['Aoyama-itchome', 'Kokuritsu-Kyogijo', 1.2],
                      ['Ginza', 'Kasumigaseki', 1.0], ['Hibiya', 'Kasumigaseki', 0.8], ['Ichigaya', 'Kudanshita', 1.3],
                      ['Iidabashi', 'Korakuen', 1.4], ['Ikebukuro', 'Kanamecho', 0.9], ['Jimbocho', 'Ogawamachi', 0.9],
                      ['Kasuga', 'Iidabashi', 1.0], ['Kasumigaseki', 'Hibiya', 0.8],
                      ['Kokkai-gijidomae', 'Akasaka', 0.8], ['Korakuen', 'Iidabashi', 1.4],
                      ['Kudanshita', 'Jimbocho', 0.6], ['Nagatacho', 'Aoyama-Itchome', 1.4],
                      ['Nakano-Sakaue', 'Nishi-Shinjuku-gochome', 1.2], ['Nihombashi', 'Ningyocho', 0.7],
                      ['Ningyocho', 'Nihombashi', 0.7], ['Omote-sando', 'Aoyama-Itchome', 1.4],
                      ['Otemachi', 'Shin-Ochanomizu', 1.3], ['Shinjuku', 'Tochomae', 0.8],
                      ['Shinjuku-sanchome', 'Akebonobashi', 1.5], ['Tameike-Sanno', 'Roppongi-Itchome', 0.9],
                      ['Aoyama-itchome', 'Roppongi', 1.3], ['Ginza', 'Higashi-Ginza', 0.4], ['Hibiya', 'Otemachi', 0.9],
                      ['Ichigaya', 'Akebonobashi', 1.4], ['Iidabashi', 'Ichigaya', 1.1],
                      ['Jimbocho', 'Kudanshita', 0.6], ['Kasumigaseki', 'Kokkai-gijidomae', 0.8],
                      ['Kudanshita', 'Ichigaya', 1.3], ['Nagatacho', 'Yotsuya', 1.3], ['Nihombashi', 'Takaracho', 0.8],
                      ['Omote-sando', 'Shibuya', 1.3], ['Otemachi', 'Nijubashimae', 0.7], ['Shinjuku', 'Yoyogi', 0.6],
                      ['Shinjuku-sanchome', 'Shinjuku', 0.8], ['Ginza', 'Hibiya', 0.4],
                      ['Hibiya', 'Uchisaiwaicho', 0.9], ['Iidabashi', 'Kasuga', 1.0],
                      ['Nagatacho', 'Tameike-Sanno', 0.9], ['Otemachi', 'Mitsukoshimae', 0.7],
                      ['Iidabashi', 'Ushigome-Kagurazaka', 1.0], ['Otemachi', 'Jimbocho', 1.7],
                      ['Otemachi', 'Jimbocho', 1.4], ['Otemachi', 'Hibiya', 0.9]]

    def adicionar_aresta(self, inicio, fim, peso):
        self.grafo.append([inicio, fim, peso])

    def mostrar_estacoes(self, distancia, origem):
        distancias = ""
        for chave, valor in distancia.items():
            if valor != float("Inf") and valor != 0:
                distancias += f"{origem} ---> {chave}: {valor:.2f} Km\n"
        return distancias

    def bellman_ford(self, inicio, fim):
        # Inicializa as distâncias e predecessores de todos os nós
        distancias = {no: float('inf') for no in self.nos}
        predecessores = {no: None for no in self.nos}
        distancias[inicio] = 0

        # Relaxa as arestas repetidamente
        for i in range(len(self.nos) - 1):
            for u, v, peso in self.grafo:
                try:
                    if distancias[u] + peso < distancias[v]:
                        distancias[v] = distancias[u] + peso
                        predecessores[v] = u
                except:
                    pass

        # Verifica se há ciclos negativos
        for u, v, peso in self.grafo:
            try:
                if distancias[u] + peso < distancias[v]:
                    raise ValueError("O grafo contém um ciclo negativo")
            except:
                pass

        # Constrói o trajeto a partir dos predecessores
        trajeto = [fim]
        no_atual = fim
        while predecessores[no_atual] is not None:
            trajeto.insert(0, predecessores[no_atual])
            no_atual = predecessores[no_atual]

        # Retorna a distância mais curta e o trajeto
        return f'{inicio} ---> {fim} : {distancias[fim]:.2f}', trajeto

    def plotar_subgrafo(self, mDistancia, mPercurso, mOption):
        if mOption == 1:
            # Executa o algoritmo Bellman-Ford
            distancia, trajeto = mDistancia, mPercurso

            # Cria um subgrafo que contém apenas os nós e as arestas no trajeto
            subgrafo = nx.DiGraph()
            for no in trajeto:
                subgrafo.add_node(no)
            for u, v, peso in self.grafo:
                if u in trajeto and v in trajeto:
                    subgrafo.add_edge(u, v, weight=peso)

            # Define o layout do grafo
            pos = nx.spring_layout(subgrafo)

            # Desenha o subgrafo com as arestas e os pesos
            nx.draw(subgrafo, pos, with_labels=True, node_color='lightblue', node_size=800, font_size=12)
            labels = nx.get_edge_attributes(subgrafo, 'weight')
            nx.draw_networkx_edge_labels(subgrafo, pos, edge_labels=labels, font_size=10)

            # Adiciona um título com a distância mais curta
            #plt.title('Distância mais curta: {:.2f}'.format(distancia))
            plt.title('Distância mais curta')

            # Mostra o gráfico
            plt.show()
        else:
            pass

        print(44 * '*')
        print("     Obrigado por usar nossos serviços!")
        print(44 * '*')
grafo = Graph(214)

def toquioMetro():
    pontoInicio = input('Digite a primeira estação: ')
    pontoFim = input('Digite a segunda estação: ')

    distancia, percurso = grafo.bellman_ford(pontoInicio, pontoFim)

    print(42*'=')
    print('Seu percurso será: ')
    for i in percurso:
        print(i)
    print(distancia)
    print(42*'=')

    menu2 = int(input('''
    VOCÊ QUER EXIBIR O SEU CAMINHO?
    [SIM(1)] [NÃO(2)]: '''))
    grafo.plotar_subgrafo(distancia, percurso, menu2)

menu = f'''
{42*'='}
       BEM VINDO AO METRO DE TÓQUIO
    FAREMOS O MELHOR TRAJETO PARA VOCÊ
{42*'='}
    '''
print(menu)


toquioMetro()

