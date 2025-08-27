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