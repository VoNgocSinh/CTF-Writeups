# Overthewire - writeups CTF

- **Challenge:** Assembly Level 1 -> 30
- **Category:** Programming languages
- **Difficulty:** Easy
- **Source**: [pwn.college](https://pwn.college/computing-101/assembly-crash-course/)

**📝Note:** Xhi chào các bạn! Trong ```writeup``` này mình sẽ chia sẻ lại hành trình học và làm các thử thách Assembly từ level 1 đến 30. Mình chọn pwn.college
 làm nơi bắt đầu vì đây là một khóa học rất trực quan, dễ tiếp cận cho người mới. Hy vọng writeup này sẽ giúp các bạn mới bắt đầu có thêm tài liệu tham khảo và cảm thấy Assembly bớt “khó nhằn” hơn. Thì trong challenge này mình sẽ học và sử dụng python và thư viện pwntools để làm các thử thách đó. Và 1 template mình sẽ sử dụng hầu hết cho toàn bộ các level là:
```python
import pwn

pwn.context.update(arch="amd64")
output = pwn.process("/challenge/run")

asm = """
    Code here
"""

output.write(pwn.asm(asm))
print(output.readallS())
```

Và trước khi bắt đầu mình có 1 vài docs và video liên quan đến Assembly các bạn có thể đọc thử tại đây:
- [LiveOverflow](https://www.youtube.com/watch?v=iyAyN3GFM7A&list=PLhixgUqwRTjxglIswKp9mpkfPNfHkzyeN&index=1)
- [Comprehensive assembly tutorial](https://github.com/mytechnotalent/Reverse-Engineering-Tutorial)
- [Architecture 1001: x86-64 Assembly](https://ost2.fyi/Arch1001)
- [x86_64 assembly book](https://open.umn.edu/opentextbooks/textbooks/733)
- ...vv

Giờ thì chúng ta bắt đầu nhé >.<

### Level 1 - set-register
---

#### Tóm tắt đề bài
Đối với level này, chúng ta sẽ phải làm việc với ```thanh ghi``` (register). Ta sẽ được sửa đổi giá trị của các ```thanh ghi```.
- ```rdi = 0x1337```
---
#### Lời giải
Bài này mình sẽ sử dụng lệnh ```mov``` (move), để gán giá trị ```0x1337``` cho thanh ghi ```rdi```.

- ```mov destination, source```

```python
import pwn

pwn.context.update(arch="amd64")
output = pwn.process("/challenge/run")

asm = """
    mov rdi, 0x1337
"""

output.write(pwn.asm(asm))
print(output.readallS())
```
---

#### Flag
```pwn.college{oKKStzagvDTco-U2z7JeqL9aJ7I.dRTOxwCMxADNwEzW}```

---

### Level 2 - set-multiple-register
---

#### Tóm tắt đề bài
Đối với level này, chúng ta sẽ phải làm việc với ```thanh ghi``` (register). Ta sẽ được sửa đổi giá trị của các ```thanh ghi```.
- ```rax = 0x1337``` <br>
- ```r12 = 0xCAFED00D1337BEEF```<br>
- ```rsp = 0x31337```
---
#### Lời giải
Bài này mình sẽ sử dụng lệnh ```mov``` (move), để gán giá trị tương ứng cho các thanh ghi:
- mov rax, 0x1337
- mov r12, 0xCAFED00D1337BEEF
- mov rsp, 0x31337

```python
import pwn

pwn.context.update(arch="amd64")
output = pwn.process("/challenge/run")

asm = """
    mov rax, 0x1337
    mov r12, 0xCAFED00D1337BEEF
    mov rsp, 0x31337
"""

output.write(pwn.asm(asm))
print(output.readallS())
```
---
#### Flag
```pwn.college{84QGDVvZkB175O8V2O8f0fLeUsT.QXwEDOzwCMxADNwEzW}```

### Level 3 - add-to-register
---

#### Tóm tắt đề bài
Đối với level này, chúng ta sẽ phải làm việc với ```thanh ghi``` (register). Ta sẽ được sửa đổi giá trị của các ```thanh ghi```.

Ta sẽ được đặt một số giá trị trong bộ nhớ ngẫu nhiên trước mỗi lần chạy. Ở mỗi lần chạy, các giá trị sẽ thay đổi. Điều này có nghĩa là ta sẽ cần thực hiện các phép toán có công thức với các thanh ghi. Chúng ta sẽ được biết thanh ghi nào được thiết lập sẵn và ta cần đặt kết quả ở đâu. Trong hầu hết các trường hợp, đó là `rax`.

Có rất nhiều lệnh trong x86 cho phép ta thực hiện tất cả các phép toán toán học thông thường trên các thanh ghi và bộ nhớ.  

Để viết ngắn gọn, khi chúng ta nói `A += B`, nó thực sự có nghĩa là `A = A + B`.
#### Đây là 1 số phép toán cơ bản trong x86:
- `add reg1, reg2` ⇔ `reg1 += reg2`
- `sub reg1, reg2` ⇔ `reg1 -= reg2`
- `imul reg1, reg2` ⇔ `reg1 *= reg2`

Lệnh `div` phức tạp hơn, chúng ta sẽ thảo luận sau.  

Lưu ý: tất cả `regX` có thể được thay thế bởi một hằng số hoặc một vị trí trong bộ nhớ.

Nhiệm vụ của bài:
- ```Add 0x331337 to rdi```

---

#### Lời giải
Bài này mình sẽ sử dụng các phép toán ```add``` được cho ở trên, để tính toán giá trị tương ứng cho thanh ghi ```rdi```:
- `add rdi, 0x331337`

```python
import pwn

pwn.context.update(arch="amd64")
output = pwn.process("/challenge/run")

asm = """
    add rdi, 0x331337
"""

output.write(pwn.asm(asm))
print(output.readallS())
```

---

#### Flag
```pwn.college{wd0wKMwgM-5ShaBXefwLGguJct2.dVTOxwCMxADNwEzW}```