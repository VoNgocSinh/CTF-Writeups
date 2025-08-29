# Overthewire - writeups CTF

- **Challenge:** Bandit Level 0 -> 33
- **Category:** Linux
- **Difficulty:** Easy
- **Source**: [Overthewire](https://overthewire.org/wargames/bandit/)

**📝Note:** Xin chào các bạn, đây là ```writeup``` đầu tiên mình viết khi mình bắt đầu với ```CTF``` và đặc biệt là ```Pwnable```. Trong bài viết này, mình xin chia sẻ với mọi người về hướng tiếp cận và cách giải của mình về 34 level ```bandit``` ở trên OverTheWire. Các thử thách của bandit chủ yếu xoay quanh các lệnh linux cơ bản, thường hay sử dụng và quan trọng là nó sẽ giúp chúng ta thực hành các vấn đề liên quan về CTF. Vì là bài writeups đầu tiên mình viết nên mong mọi người góp ý.

### Level 0
Level này yêu cầu mình sử dụng ```ssh``` để kết nối vào server ```bandit.labs.overthewire.org``` với port ```2220```, username và password là ```bandit0```.
![alt text](img/level0.png)

#### Solution
Để kết nối vào server với cổng port 2220 ta sẽ sử dụng thêm option ```-p 2220``` (-p tức là port).

```ssh bandit0@bandit.labs.overthewire.org -p 2220```

Sau đó màn hình sẽ hiện ra yêu cầu nhập pass và khi đó ta chỉ cần nhập pass ```bandit0``` là được.

![alt text](img/level0-1.png)

####  References
- [Secure Shell (SSH) on Wikipedia](https://en.wikipedia.org/wiki/Secure_Shell) <br>
- [How to use SSH on wikiHow](https://www.wikihow.com/Use-SSH)

### Level 0 -> level 1
Yeh, sau khi kết nối được vào server thì nó bảo có 1 file có tên là ```readme``` ngay tại thư mục ```home``` chứa password cho level tiếp theo. Và tương tự như vậy, dù ở bất cứ level nào, bạn cần tìm password được giấu ở đâu đó, sau đó ```ssh``` để kết nối tới level tiếp theo.
![alt text](img/level0-2.png)

#### Solution
Trước khi giải quyết level này ta cần tìm hiểu về 1 số lệnh sau:
- ```ls```: dùng để xem các file hiện có trong folder
- ```cd```: dùng để di chuyển tới các folder cụ thể
- ```cat```: dùng để xem nội dung của file
- ```file```: dùng để xem kiểu file
- ```du```: dùng để xem dung lượng file và folder
- ```find```: dùng để tìm kiếm file và folder

![alt text](img/level0-3.png)
Với 1 số lệnh trên, đầu tiên mình đã thử dùng ```ls``` để xem ở trong folder hiện tại có những file gì thì bất giờ file ```readme``` có ngay ở đây, và sau đó mình dùng ```cat``` để in ra nội dung của file ```readme``` đó. 

Password cho level tiếp theo được hiện ra. (```ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If```)

### Level 1 -> level 2
Level này yêu cầu ta mở file có tên là '```-```' được lưu trong folder ```home```.
![alt text](img/level1.png)
#### Solution
Đối với level này mình sẽ sử dụng lệnh ```cat``` để in password được lưu trong file '```-```' (dashed filename). Tuy nhiên, nếu mình sử dụng ```cat -``` như thông thường, thì nó sẽ không in ra gì cả vì nó sẽ hiểu một cách đặc biệt là lệnh đọc dữ liệu từ bàn phím (stdin) . Vậy nên nếu muốn in ra nội dung của file '```-```' ta cần chỉ rõ đường dẫn của file '```-```'. <br><br>
Cụ thể: ```cat ./-```

![alt text](img/level1-1.png)
Password cho level tiếp theo được hiện ra. (```263JGJPfgU6LtdEvgfWU1XP5yac29mFx```)

####  References
- [Google Search for "dashed filename"](https://www.google.com/search?q=dashed+filename)
- [Advanced Bash-scripting Guide - Chapter 3 - Special Characters](https://linux.die.net/abs-guide/special-chars.html)

### Level 2 -> level 3
Level này yêu cầu ta mở file có tên là ```--spaces in this filename--``` được lưu trong folder ```home```.
![alt text](img/level2.png)
#### Solution
Đối với level này mình sẽ sử dụng ```cat``` để in password được lưu trong file ```--spaces in this filename--``` nhưng ta không thể truy cập folder hoặc file có khoảng cách 1 cách bình thường như vậy mà phải chỉ rõ đường dẫn file và thêm ký tự '```\```' vào trước mỗi khoảng cách.<br>
Cụ thể: ```cat ./--spaces\ in\ this\ filename--```

Ngoài ra, có 1 cách khác là mình có thể thêm 2 dấu nháy đơn(hoặc kép) vào 2 đầu của đường dẫn file đó.<br>
Cụ thể: ```cat './--spaces in this filename--```

![alt text](img/level2-1.png)

Password cho level tiếp theo được hiện ra. (```MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx```)

####  References
- [Google Search for “spaces in filename”](https://www.google.com/search?q=spaces+in+filename)
- [Dealing With Spaces in Filenames in Linux
](https://linuxhandbook.com/filename-spaces-linux/)

### Level 3 -> level 4

Level này yêu cầu ta mở hidden file được giấu trong folder ```inhere``` để lấy được password cho level tiếp theo.
![alt text](img/level3.png)

#### Solution
Đối với level này mình sẽ sử dụng ```ls``` để xem các file có trong folder ```inhere``` tuy nhiên, nếu chỉ sử dụng ```ls``` bình thường mà không truyền vào options nào thì nó sẽ không hiện đầy đủ các file (không hiện hidden file). Vì vậy, sau khi tìm hiểu thì mình thấy để hiện đầy đủ các file có trong 1 folder thì ta phải thêm option ```-a``` (all) vào.<br>
Cụ thể: ```ls -a inhere```

![alt text](img/level3-1.png) <br>

Password cho level tiếp theo được hiện ra. (```2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ```)

### Level 4 -> level 5
Level này yêu cầu ta mở file duy nhất có thể đọc trong số các file ở trong folder ```inhere``` để có thể lấy được password cho level tiếp.

![alt text](img/level4.png)

#### Solution
Như theo mô tả đề bài ta có thể thấy, chỉ có duy nhất 1 file có thể đọc. Vì vậy, ta sử dụng lệnh ```file``` để có thể in ra thông tin về file đó. Và đặc biệt hơn, trong bài này có tận 10 file khác nhau nên cách tốt nhất để in ra các thông tin của các file trong cùng 1 lần ta có thể truyền vào đường dẫn như sau.<br>
Cụ thể: ```file ./inhere/*```<br>
```*``` trong trường hợp này có ý nghĩa là nó sẽ bao gồm tất cả các file có ở trong folder ```inhere```.

![alt text](img/level4-1.png)

Password cho level tiếp theo được hiện ra. (```4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw```)

### Level 5 -> level 6

Level này yêu cầu ta cần tìm password được lưu trong 1 file và được lưu dưới 1 folder. Ngoài ra, ta được cung cấp thêm thông tin là file đó có các thông tin về file như:
- human-readable (File đó có thể đọc)
- 1033 bytes in size (File có kích thước 1033byte)
- not executable (File đó không thể thực thi)

![alt text](img/level5.png)

#### Solution
Dựa trên các thông tin mà file đó cung cấp, ta có thể brute-force để tìm file có đầy đủ các thông tin đó=)). Hoặc cách để tìm cách tốt hơn thì ta có thể lọc ra các file có các thông tin đó.

1. ```human-readable```: ta có thể sử dụng lệnh ```file``` in ra thông tin các file sau đó kết hợp sử dụng lệnh ```grep``` để lọc ra các file có dạng dữ liệu là ```ASCII text```.<br> Cụ thể: ```file */* | grep "ASCII text"```
![alt text](img/level5-1.png)
2. ```1033 bytes in size```: ta có thể sử dụng lệnh ```find``` để tìm các file với option ```-size 1033c```. (1033c tức là 1033bytes)<br>
Cụ thể: ```find . -size 1033c```
![alt text](img/level5-2.png)
3. ```not executable```: ta có thể sử dụng lệnh ```find``` để tìm các file với option ```-executable```. (File không thể thực thi) <br>
Cụ thể: ```find . -executable```
![alt text](img/level5-3.png)

Như vậy, đối với 2 thông tin ```human-readable``` và ```not executable``` thì có rất nhiều file có thông tin đó, tuy nhiên đối với thông tin ```1033 bytes in size``` thì chỉ có duy nhất 1 file là ```./maybehere07/.file2```. Vì vậy ta có thể chọn thông tin này để tìm kiếm file đó là cách tốt nhất.

![alt text](img/level5-4.png)

Password cho level tiếp theo được hiện ra. (```HWasnPhtq9AVKe0dmk45nxy20cvUa6EG```)

