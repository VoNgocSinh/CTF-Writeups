# Overthewire - writeups CTF

- **Challenge:** Bandit Level 0 -> 33
- **Category:** Linux
- **Difficulty:** Easy
- **Source**: [Overthewire](https://overthewire.org/wargames/bandit/)

**📝Note:** Xin chào các bạn, đây là ```writeup``` đầu tiên mình viết khi mình bắt đầu với ```CTF``` và đặc biệt là ```Pwnable```. Trong bài viết này, mình xin chia sẻ với mọi người về hướng tiếp cận và cách giải của mình về 34 level ```bandit``` ở trên OverTheWire. Các thử thách của bandit chủ yếu xoay quanh các lệnh linux cơ bản, thường hay sử dụng và quan trọng là nó sẽ giúp chúng ta thực hành các vấn đề liên quan về CTF. Vì là bài writeups đầu tiên mình viết nên mong mọi người góp ý.

### 🚩Level 0
Cấp độ này yêu cầu mình sử dụng ```ssh``` để kết nối vào server ```bandit.labs.overthewire.org``` với port ```2220```, username và password là ```bandit0```.
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
Yeh, sau khi kết nối được vào server thì nó bảo có 1 file có tên là ```readme``` ngay tại thư mục ```home``` chứa password cho cấp độ tiếp theo. Và tương tự như vậy, dù ở bất cứ cấp độ nào, bạn cần tìm password được giấu ở đâu đó, sau đó ```ssh``` để kết nối tới cấp độ tiếp theo.
![alt text](img/level0-2.png)

#### 💁Solution
Một số lệnh hữu ích để giải quyết level này là:
- ```ls```: dùng để xem các file hiện có trong folder
- ```cd```: dùng để di chuyển tới các folder cụ thể
- ```cat```: dùng để xem nội dung của file
- ```file```: dùng để xem kiểu file
- ```du```: dùng để xem dung lượng file và folder
- ```find```: dùng để tìm kiếm file và folder

![alt text](img/level0-3.png)
Với 1 số lệnh trên, đầu tiên mình đã thử dùng ```ls``` để xem ở trong folder hiện tại có những file gì thì bất giờ file readme có ngay ở đây, và sau đó mình dùng ```cat``` để in ra nội dung của file ```readme``` đó. 

Và password cho level tiếp theo được hiện ra. (```ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If```)
