# Overthewire - writeups CTF

- **Challenge:** Bandit Level 0 -> 33
- **Category:** Linux
- **Difficulty:** Easy
- **Source**: [Overthewire](https://overthewire.org/wargames/bandit/)

**📝Note:** Xin chào các bạn, đây là ```writeup``` đầu tiên mình viết khi mình bắt đầu với ```CTF``` và đặc biệt là ```Pwnable```. Trong bài viết này, mình xin chia sẻ với mọi người về hướng tiếp cận và cách giải của mình về 34 level ```bandit``` ở trên OverTheWire. Các thử thách của bandit chủ yếu xoay quanh các lệnh linux cơ bản, thường hay sử dụng và quan trọng là nó sẽ giúp chúng ta thực hành các vấn đề liên quan về CTF. Vì là bài writeups đầu tiên mình viết nên mong mọi người góp ý.

### 🚩Level 0
Level này yêu cầu mình sử dụng ```ssh``` để kết nối vào server ```bandit.labs.overthewire.org``` với port ```2220```, username và password là ```bandit0```.
![alt text](img/level0.png)

#### 💁Solution
Để kết nối vào server với cổng port 2220 ta sẽ sử dụng thêm option ```-p 2220``` (-p tức là port).

```ssh bandit0@bandit.labs.overthewire.org -p 2220```

Sau đó màn hình sẽ hiện ra yêu cầu nhập pass và khi đó ta chỉ cần nhập pass ```bandit0``` là được.

![alt text](img/level0-1.png)

####  📌References
- [Secure Shell (SSH) on Wikipedia](https://en.wikipedia.org/wiki/Secure_Shell) <br>
- [How to use SSH on wikiHow](https://www.wikihow.com/Use-SSH)

### 🚩Level 0 -> level 1
Yeh, sau khi kết nối được vào server thì nó bảo có 1 file có tên là ```readme``` ngay tại thư mục ```home``` chứa password cho level tiếp theo. Và tương tự như vậy, dù ở bất cứ level nào, bạn cần tìm password được giấu ở đâu đó, sau đó ```ssh``` để kết nối tới level tiếp theo.
![alt text](img/level0-2.png)

#### 💁Solution
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

### 🚩Level 1 -> level 2
Level này yêu cầu ta mở file có tên là '```-```' được lưu trong folder ```home```.
![alt text](img/level1.png)
#### 💁Solution
Đối với level này mình sẽ sử dụng lệnh ```cat``` để in password được lưu trong file '```-```' (dashed filename). Tuy nhiên, nếu mình sử dụng ```cat -``` như thông thường, thì nó sẽ không in ra gì cả vì nó sẽ hiểu một cách đặc biệt là lệnh đọc dữ liệu từ bàn phím (stdin) . Vậy nên nếu muốn in ra nội dung của file '```-```' ta cần chỉ rõ đường dẫn của file '```-```'. <br><br>
Cụ thể: ```cat ./-```

![alt text](img/level1-1.png)
Password cho level tiếp theo được hiện ra. (```263JGJPfgU6LtdEvgfWU1XP5yac29mFx```)

####  📌References
- [Google Search for "dashed filename"](https://www.google.com/search?q=dashed+filename)
- [Advanced Bash-scripting Guide - Chapter 3 - Special Characters](https://linux.die.net/abs-guide/special-chars.html)

### 🚩Level 2 -> level 3
Level này yêu cầu ta mở file có tên là ```--spaces in this filename--``` được lưu trong folder ```home```.
![alt text](img/level2.png)
#### 💁Solution
Đối với level này mình sẽ sử dụng ```cat``` để in password được lưu trong file ```--spaces in this filename--``` nhưng ta không thể truy cập folder hoặc file có khoảng cách 1 cách bình thường như vậy mà phải chỉ rõ đường dẫn file và thêm ký tự '```\```' vào trước mỗi khoảng cách.<br>
Cụ thể: ```cat ./--spaces\ in\ this\ filename--```

Ngoài ra, có 1 cách khác là mình có thể thêm 2 dấu nháy đơn(hoặc kép) vào 2 đầu của đường dẫn file đó.<br>
Cụ thể: ```cat './--spaces in this filename--```

![alt text](img/level2-1.png)

Password cho level tiếp theo được hiện ra. (```MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx```)

####  📌References
- [Google Search for “spaces in filename”](https://www.google.com/search?q=spaces+in+filename)
- [Dealing With Spaces in Filenames in Linux
](https://linuxhandbook.com/filename-spaces-linux/)