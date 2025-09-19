# Pwn.college - writeups CTF

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

---

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

---

### Level 4 - linear-equation-register

---

#### Tóm tắt đề bài
Đối với level này, chúng ta sẽ phải làm việc với ```thanh ghi``` (register). Ta sẽ được sửa đổi giá trị của các ```thanh ghi```.

Chúng ta sẽ đặt một số giá trị trong bộ nhớ một cách động trước mỗi lần chạy. Mỗi lần chạy, các giá trị này sẽ thay đổi. Điều này có nghĩa là ta sẽ cần phải thực hiện một số phép toán công thức với các thanh ghi. Ta sẽ được biết thanh ghi nào được thiết lập trước và ta nên đặt kết quả vào đâu. Trong hầu hết các trường hợp, đó là `rax`.

`Lưu ý:` Có một sự khác biệt quan trọng giữa `mul` (nhân không dấu) và `imul` (nhân có dấu) về việc các thanh ghi nào được sử dụng. Hãy xem tài liệu của các lệnh này để thấy sự khác biệt.

Trong trường hợp này, mình sẽ dùng `imul`.

Nhiệm vụ của bài:
- `f(x) = mx + b`, trong đó:  
  - `m = rdi  `
  - `x = rsi`
  - `b = rdx ` 
- Đặt kết quả vào `rax`.

---

#### Lời giải
Bài này mình sẽ sử dụng các phép toán ```add```, ```mov``` và ```imul``` được cho ở trên, để tính toán giá trị tương ứng cho thanh ghi ```rdi```:
- ```mov rax, rdi```
- ```imul rax, rsi```
- ```add rax, rdx```
```python
import pwn

pwn.context.update(arch="amd64")
output = pwn.process("/challenge/run")

asm = """
    mov rax, rdi
    imul rax, rsi
    add rax, rdx
"""

output.write(pwn.asm(asm))
print(output.readallS())
```

---

#### Flag
```pwn.college{Ak972rqZI3bTT3lQaA-NewS-9el.dZTOxwCMxADNwEzW}```

---

### Level 5 - integer-division

---

#### Tóm tắt đề bài
Đối với level này, chúng ta sẽ phải làm việc với ```thanh ghi``` (register). Ta sẽ được sửa đổi giá trị của các ```thanh ghi```.

Chúng ta sẽ đặt một số giá trị trong bộ nhớ một cách động trước mỗi lần chạy. Mỗi lần chạy, các giá trị này sẽ thay đổi. Điều này có nghĩa là ta sẽ cần phải thực hiện một số phép toán công thức với các thanh ghi. Ta sẽ được biết thanh ghi nào được thiết lập trước và ta nên đặt kết quả vào đâu. Trong hầu hết các trường hợp, đó là `rax`.

Phép chia trong `x86` đặc biệt hơn so với toán học bình thường. Ở đây gọi là phép chia số nguyên, nghĩa là mọi giá trị đều là số nguyên.

Ví dụ: `10 / 3 = 3` trong toán số nguyên.  

Tại sao?  
Vì 3.33 được làm tròn xuống thành số nguyên.

Các lệnh liên quan trong cấp độ này là:  

- `mov rax, reg1`  
- `div reg2`  

`Lưu ý:` `div` là một lệnh đặc biệt có thể chia số bị chia `128-bit` cho số chia `64-bit`, đồng thời lưu cả thương và số dư, chỉ dùng một thanh ghi làm toán hạng.

Lệnh `div` hoạt động như sau (khi chia cho `reg`):  

- `rax = rdx:rax / reg`  
- `rdx = remainder`  

`rdx:rax` nghĩa là `rdx` sẽ chứa 64-bit cao của số bị chia 128-bit và `rax` chứa 64-bit thấp của số bị chia 128-bit.

Bạn phải cẩn thận với những gì nằm trong `rdx` và `rax` trước khi gọi `div`.  

Nhiệm vụ của bài:

- `speed = distance / time`, trong đó:  
  - `distance = rdi ` 
  - `time = rsi  `
  - `speed = rax  `

`Lưu ý:` Vì `distance` luôn nằm trong phạm vi 64-bit, nên `rdx` cần được đặt bằng 0 trước khi thực hiện phép chia.

---

#### Lời giải

Bài này mình sẽ sử dụng các phép toán ```div```, ```mov``` được cho ở trên, để tính toán giá trị tương ứng cho thanh ghi ```rax```:
-   `mov rax, rdi`
-   `div rsi`
```python
import pwn

pwn.context.update(arch="amd64")
output = pwn.process("/challenge/run")

asm = """
    mov rax, rdi
    div rsi
"""

output.write(pwn.asm(asm))
print(output.readallS())
```

---

#### Flag
```pwn.college{k590aWudsmdyuMBfYxWEXaX5CFV.ddTOxwCMxADNwEzW}```

---

### Level 6 - modulo-operation

#### Tóm tắt đề bài
Đối với level này, chúng ta sẽ phải làm việc với ```thanh ghi``` (register). Ta sẽ được sửa đổi giá trị của các ```thanh ghi```.

Chúng ta sẽ đặt một số giá trị trong bộ nhớ một cách động trước mỗi lần chạy. Mỗi lần chạy, các giá trị này sẽ thay đổi. Điều này có nghĩa là ta sẽ cần phải thực hiện một số phép toán công thức với các thanh ghi. Ta sẽ được biết thanh ghi nào được thiết lập trước và ta nên đặt kết quả vào đâu. Trong hầu hết các trường hợp, đó là `rax`.

Modulo trong assembly là một khái niệm thú vị khác!  

x86 cho phép bạn lấy phần dư sau một phép chia `div`.  

Ví dụ: `10 / 3` cho kết quả dư là `1`.  

Phần dư này chính là phép modulo, hay còn gọi là toán tử `mod`.  

Trong hầu hết các ngôn ngữ lập trình, chúng ta biểu diễn mod bằng ký hiệu `%`.

Nhiệm vụ của bài:

- `rdi % rsi`
- Đặt kết quả vào `rax`.

---

#### Lời giải

Bài này mình sẽ sử dụng các phép toán ```div```, ```mov``` được cho ở trên, để tính toán giá trị tương ứng cho thanh ghi ```rax```:
-   `mov rax, rdi`
-   `div rsi`
-   `mov rax, rdx`
```python
import pwn

pwn.context.update(arch="amd64")
output = pwn.process("/challenge/run")

asm = """
    mov rax, rdi
    div rsi
    mov rax, rdx    #phan du duoc luu o thanh ghi rdx
"""

output.write(pwn.asm(asm))
print(output.readallS())
```

---

#### Flag
```pwn.college{UntmBM38D5Ptt8Zj2WkyZBKqrCx.dhTOxwCMxADNwEzW}```

---

### Level 7 - set-upper-byte

---

#### Tóm tắt đề bài

Đối với level này, chúng ta sẽ phải làm việc với ```thanh ghi``` (register). Ta sẽ được sửa đổi giá trị của các ```thanh ghi```.

Chúng ta sẽ đặt một số giá trị trong bộ nhớ một cách động trước mỗi lần chạy. Mỗi lần chạy, các giá trị này sẽ thay đổi. Điều này có nghĩa là ta sẽ cần phải thực hiện một số phép toán công thức với các thanh ghi. Ta sẽ được biết thanh ghi nào được thiết lập trước và ta nên đặt kết quả vào đâu. Trong hầu hết các trường hợp, đó là `rax`.

Một khái niệm thú vị khác trong x86 là khả năng truy cập độc lập vào các byte thấp hơn của thanh ghi.

Mỗi thanh ghi trong x86_64 có kích thước 64 bit, và trong các cấp độ trước, chúng ta đã truy cập toàn bộ thanh ghi bằng `rax`, `rdi`, hoặc `rsi`.

Chúng ta cũng có thể truy cập các byte thấp hơn của mỗi thanh ghi bằng các tên thanh ghi khác nhau.  

Ví dụ, 32 bit thấp của `rax` có thể được truy cập bằng `eax`, 16 bit thấp bằng `ax`, và 8 bit thấp bằng `al`.  

```
MSB                                  LSB
+--------------------------------------+
|                 rax                  |
+------------------+-------------------+
                   |        eax        |
                   +---------+---------+
                             |    ax   |
                             +----+----+
                             | ah | al |
                             +----+----+                             
```


Việc truy cập byte thấp của thanh ghi áp dụng cho hầu hết tất cả các thanh ghi.  

Nhiệm vụ của bài:
- Chỉ với một lệnh `mov`, hãy đặt 8 bit cao của thanh ghi `ax` thành `0x42`.

---

#### Lời giải

Bài này mình sẽ sử dụng các phép toán ```mov``` được cho ở trên, để tính toán giá trị tương ứng cho thanh ghi ```ah```:
-  `mov ah, 0x42` 

```python
import pwn

pwn.context.update(arch="amd64")
output = pwn.process("/challenge/run")

asm = """
    mov ah, 0x42    #8 bit cao cua ax la ah
"""

output.write(pwn.asm(asm))
print(output.readallS())
```

---

#### Flag
```pwn.college{E34v0I-pMN4AVn6Rb53gNjWOpmw.QXxEDOzwCMxADNwEzW}```

---

### Level 8 - efficient-modulo

---

#### Tóm tắt đề bài
Đối với level này, chúng ta sẽ phải làm việc với ```thanh ghi``` (register). Ta sẽ được sửa đổi giá trị của các ```thanh ghi```.

Chúng ta sẽ đặt một số giá trị trong bộ nhớ một cách động trước mỗi lần chạy. Mỗi lần chạy, các giá trị này sẽ thay đổi. Điều này có nghĩa là ta sẽ cần phải thực hiện một số phép toán công thức với các thanh ghi. Ta sẽ được biết thanh ghi nào được thiết lập trước và ta nên đặt kết quả vào đâu. Trong hầu hết các trường hợp, đó là `rax`.

Thì ra việc sử dụng lệnh `div` để tính toán phép modulo là chậm!  

Chúng ta có thể dùng một mẹo toán học để tối ưu toán tử modulo (`%`). Trình biên dịch thường xuyên sử dụng mẹo này.  

Nếu chúng ta có `x % y`, và `y` là một lũy thừa của 2 (chẳng hạn `2^n`), thì kết quả sẽ chính là `n` bit thấp nhất của `x`.  

Vì vậy, chúng ta có thể dùng quyền truy cập vào byte thấp của thanh ghi để thực hiện modulo một cách hiệu quả!  

Chỉ được sử dụng lệnh sau:  

- `mov`  

Nhiệm vụ của bài:  

- `rax = rdi % 256`  
- `rbx = rsi % 65536`

---

#### Lời giải

Bài này mình sẽ sử dụng các phép toán ```mov``` được cho ở trên, để tính toán giá trị tương ứng cho thanh ghi `rax` và `rbx`:

Ta có:
- `256 = 2^8`
- `65536 = 2^16`

Vì thế, mình sẽ lấy 8 bit thấp nhất của `rdi` và 16 bit thấp nhất của `rsi`.

- `mov al, dil`
- `mov bx, si`

```python
import pwn

pwn.context.update(arch="amd64")
output = pwn.process("/challenge/run")

asm = """
   mov al, dil
   mov bx, si
"""

output.write(pwn.asm(asm))
print(output.readallS())
```

---

#### Flag
```pwn.college{UcxGOiYmVzsdZRrWtZhnqEpNRze.dlTOxwCMxADNwEzW}```

---

### Level 9 - byte-extraction

---

#### Tóm tắt đề bài

Đối với level này, chúng ta sẽ phải làm việc với ```thanh ghi``` (register). Ta sẽ được sửa đổi giá trị của các ```thanh ghi```.

Chúng ta sẽ đặt một số giá trị trong bộ nhớ một cách động trước mỗi lần chạy. Mỗi lần chạy, các giá trị này sẽ thay đổi. Điều này có nghĩa là ta sẽ cần phải thực hiện một số phép toán công thức với các thanh ghi. Ta sẽ được biết thanh ghi nào được thiết lập trước và ta nên đặt kết quả vào đâu. Trong hầu hết các trường hợp, đó là `rax`.

Trong cấp độ này, bạn sẽ làm việc với `toán tử logic và bit`. Điều này sẽ liên quan nhiều đến việc tương tác trực tiếp với các bit được lưu trong thanh ghi hoặc vị trí bộ nhớ. Bạn cũng sẽ cần sử dụng các lệnh logic trong x86: `and`, `or`, `not`, `xor`.

`Dịch chuyển bit` trong assembly là một khái niệm thú vị khác!  

x86 cho phép bạn "dịch chuyển" các bit trong một thanh ghi.  

Ví dụ: `al`, tức là 8 bit thấp nhất (least significant 8 bits) của `rax`.  

Giả sử giá trị trong `al` là:  
- `rax = 10001010`


Nếu chúng ta dịch sang trái 1 lần bằng lệnh `shl`:  
- `shl al, 1`

Giá trị mới sẽ là:  
- `al = 00010100`


Tất cả các bit được dịch sang trái, và bit cao nhất (most significant bit) sẽ rơi ra, trong khi một bit 0 mới được thêm vào bên phải.  

Bạn có thể dùng thao tác này để làm những điều đặc biệt với các bit mà bạn quan tâm.  

Dịch bit còn có tác dụng phụ hữu ích: thực hiện nhân nhanh (×2) hoặc chia nhanh (÷2), và có thể dùng để tính modulo.  

Các lệnh quan trọng:

- `shl reg1, reg2` ⇔ Dịch trái `reg1` theo số lần trong `reg2`.  
- `shr reg1, reg2` ⇔ Dịch phải `reg1` theo số lần trong `reg2`.  

Lưu ý: `reg2` có thể là hằng số hoặc vị trí bộ nhớ.  

Khi nói về `significant bit` hoặc `least significant byte`, ý nghĩa là:  

- `Least significant bit/byte` mang giá trị nhỏ nhất (vị trí "thấp nhất"). Khi bạn thay đổi bit "thấp nhất" hoặc "bên phải nhất", giá trị chỉ thay đổi 1 đơn vị.  
- `Most significant bit/byte` mang giá trị lớn nhất (vị trí "cao nhất").  

Chỉ được sử dụng các lệnh sau:  
- `mov`, `shr`, `shl`

Nhiệm vụ của bài:

- Hãy thực hiện: Đặt `rax` bằng byte thấp thứ 5 của `rdi`.  

Ví dụ:
- `rdi = | B7 | B6 | B5 | B4 | B3 | B2 | B1 | B0 |`
- Set `rax` to the value of `B4`

---

#### Lời giải

Bài này mình sẽ sử dụng các phép toán ```mov```, ```shr``` và ```shl``` được cho ở trên để tính toán giá trị tương ứng cho thanh ghi `rax`:
-  ```shr rdi, 32```
-  `mov rax, 0`
-  `mov al, dil`

```python
import pwn

pwn.context.update(arch="amd64")
output = pwn.process("/challenge/run")

asm = """
   shr rdi, 32  #dich sang phai 4 byte = 32 bit
   mov rax, 0
   mov al, dil
"""

output.write(pwn.asm(asm))
print(output.readallS())
```

---

#### Flag
```pwn.college{w-kROQ6JPZk10q1XBo_dfR7Wocv.dBDMywCMxADNwEzW}```

---

### Level 10 - bitwise-and

---

#### Tóm tắt đề bài

Đối với level này, chúng ta sẽ phải làm việc với ```thanh ghi``` (register). Ta sẽ được sửa đổi giá trị của các ```thanh ghi```.

Chúng ta sẽ đặt một số giá trị trong bộ nhớ một cách động trước mỗi lần chạy. Mỗi lần chạy, các giá trị này sẽ thay đổi. Điều này có nghĩa là ta sẽ cần phải thực hiện một số phép toán công thức với các thanh ghi. Ta sẽ được biết thanh ghi nào được thiết lập trước và ta nên đặt kết quả vào đâu. Trong hầu hết các trường hợp, đó là `rax`.

Trong cấp độ này, bạn sẽ làm việc với `toán tử logic và bit`. Điều này sẽ liên quan nhiều đến việc tương tác trực tiếp với các bit được lưu trong thanh ghi hoặc vị trí bộ nhớ. Bạn cũng sẽ cần sử dụng các lệnh logic trong x86: `and`, `or`, `not`, `xor`.

`Logic bitwise trong assembly` là một khái niệm thú vị khác!  
x86 cho phép bạn thực hiện các phép toán logic từng bit trên các thanh ghi.  

Ví dụ, giả sử thanh ghi chỉ lưu 8 bit:  

- `rax = 10101010`  
- `rbx = 00110011`  

Nếu chúng ta thực hiện phép `AND` từng bit giữa `rax` và `rbx` bằng lệnh `and rax, rbx`, kết quả sẽ được tính bằng cách AND từng cặp bit một với nhau.  

Ví dụ từ trái sang phải:  

- `1 AND 0 = 0`  
- `0 AND 0 = 0`  
- `1 AND 1 = 1`  
- `0 AND 1 = 0`  
- ...  

Kết hợp tất cả kết quả, ta được:  
- `rax = 00100010`

Bảng chân trị tham khảo:

**AND**

```
| A | B | X |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |
```

**OR**

```
| A | B | X |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |
```


**XOR**

```
| A | B | X |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |
```

Không được sử dụng các lệnh sau: `mov`, `xchg`.  

Nhiệm vụ của bài:

- Đặt `rax` bằng giá trị của `(rdi AND rsi)`.  

`Lưu ý:` `rax` ban đầu sẽ có tất cả bit = 1. Nếu không, thì cấp độ này sẽ khó hơn nhiều!


--- 

#### Lời giải

Bài này mình sẽ sử dụng phép toán ```and``` được cho ở trên để tính toán giá trị tương ứng cho thanh ghi `rax`:
-  `and rax, rdi`
-  `and rax, rsi`
```python
import pwn

pwn.context.update(arch="amd64")
output = pwn.process("/challenge/run")

asm = """
   and rax, rdi   #tuong tu nhu gan rax = rdi vi hien tai tat cac biet cua rax deu bat
   and rax, rsi
"""

output.write(pwn.asm(asm))
print(output.readallS())
```

---

#### Flag
```pwn.college{EYNEn4Q0ZT_DCYkvsXmNA-4vuXl.dFDMywCMxADNwEzW}```

---

### Level 11 - check-even

---

#### Tóm tắt đề bài

Đối với level này, chúng ta sẽ phải làm việc với ```thanh ghi``` (register). Ta sẽ được sửa đổi giá trị của các ```thanh ghi```.

Chúng ta sẽ đặt một số giá trị trong bộ nhớ một cách động trước mỗi lần chạy. Mỗi lần chạy, các giá trị này sẽ thay đổi. Điều này có nghĩa là ta sẽ cần phải thực hiện một số phép toán công thức với các thanh ghi. Ta sẽ được biết thanh ghi nào được thiết lập trước và ta nên đặt kết quả vào đâu. Trong hầu hết các trường hợp, đó là `rax`.

Trong cấp độ này, bạn sẽ làm việc với `toán tử logic và bit`. Điều này sẽ liên quan nhiều đến việc tương tác trực tiếp với các bit được lưu trong thanh ghi hoặc vị trí bộ nhớ. Bạn cũng sẽ cần sử dụng các lệnh logic trong x86: `and`, `or`, `not`, `xor`.

`Logic bitwise trong assembly` là một khái niệm thú vị khác!  
x86 cho phép bạn thực hiện các phép toán logic từng bit trên các thanh ghi.  

Chỉ được sử dụng các toán tử sau:
- and
- or
- xor

Nhiệm vụ của bài:

    if x is even then
      y = 1
    else
      y = 0

    trong đó:
    - x = rdi
    - y = rax

--- 

#### Lời giải

Bài này mình sẽ sử dụng các phép toán ```and```, ```or```, ```xor``` được cho ở trên để tính toán giá trị tương ứng cho thanh ghi `rax`:
-   and rdi, 0x1
-   and rax, 0  
-   or rax, 1
-   xor rax, rdi
```python
import pwn

pwn.context.update(arch="amd64")
output = pwn.process("/challenge/run")

asm = """
    and rdi, 0x1
    and rax, 0  
    or rax, 1
    xor rax, rdi
"""

output.write(pwn.asm(asm))
print(output.readallS())
```

---

#### Flag
```pwn.college{EewjQFGPUt2YchIAoHKMHduGOTg.dJDMywCMxADNwEzW}```

---

### Level 12 - memory-read

---

#### Tóm tắt đề bài

Đối với level này, chúng ta sẽ phải làm việc với ```thanh ghi``` (register). Ta sẽ được sửa đổi giá trị của các ```thanh ghi```.

Chúng ta sẽ đặt một số giá trị trong bộ nhớ một cách động trước mỗi lần chạy. Mỗi lần chạy, các giá trị này sẽ thay đổi. Điều này có nghĩa là ta sẽ cần phải thực hiện một số phép toán công thức với các thanh ghi. Ta sẽ được biết thanh ghi nào được thiết lập trước và ta nên đặt kết quả vào đâu. Trong hầu hết các trường hợp, đó là `rax`.

Trong cấp độ này, bạn sẽ làm việc với `memory`. Điều này sẽ yêu cầu bạn sẽ đọc và ghi dữ liệu được lưu trong `memory`. Tuy nhiên nếu bạn có hơi bối rối, hãy nhìn vào địa chỉ tuyến tính (linear addressing). Bạn cũng có thể được yêu cầu hủy bỏ tham chiếu nhiều lần đến những thứ chúng tôi lưu vào bộ nhớ để bạn sử dụng.

Cho đến bây giờ, bạn đã làm việc với thanh ghi như cách để lưu mọi thứ, về cơ bản là như các biến số 'x' như trong toán học.

Tuy nhiên, chúng ta cũng có thể lưu các bytes vào trong `memory`.

Nhớ lại rằng `memory` có thể được giải quyết, và mỗi địa chỉ nó lưu 1 giá trị gì đó tại địa chỉ đó. Lưu ý rằng điều này tương tự như các địa chỉ trong đời sống.

Ví dụ như: địa chỉ `699 S Mill Ave, Tempe, AZ 85281` là địa chỉ trên bản đồ của `ASU Brickyard`. Chúng ta cũng gọi nó là 1 điểm tới `ASU Brickyard`. Chúng ta có thể biểu diễn nó như sau:

    ['699 S Mill Ave, Tempe, AZ 85281'] = 'ASU Brickyard'

Địa chỉ là đặc biệt bởi vì nó là duy nhất. Nhưng điều đó cũng không có nghĩa là các địa chỉ khác không có cùng 1 data. (Như kiểu 1 người có nhiều ngôi nhà).

Memory cũng giống y hệt như vậy.

Ví dụ như: địa chỉ trong memory, nơi mà code của bạn được lưu ở ```0x400000```. <br>
Trong `x86`, chúng ta có thể truy cập vào địa chỉ của memory, gọi là hủy tham chiếu, giống như:

    mov rax, [some_address]        <=>     Moves the thing at 'some_address' into rax

Điều này cũng hoạt động với những thứ được lưu trong các thanh ghi:

    mov rax, [rdi]         <=>     Moves the thing stored at the address of what rdi holds to rax

Tương tư, điều này cũng hoạt động để ghi vào memory:

    mov [rax], rdi         <=>     Moves rdi to the address of what rax holds.

Vì vây, nếu ```rax``` là `0xdeadbeef`, thì `rdi` sẽ lưu giá trị tại địa chỉ `0xdeadbeef`:

    [0xdeadbeef] = rdi

Lưu ý: Memory là tuyến tính, và trong x86_64, nó sẽ được đánh dấu từ 0 tới 0xffffffffffffffff (Ye, rất lớn)

Nhiệm vụ của bài:
- Đặt giá trị được lưu ở 0x404000 vào trong thanh ghi `rax`. Làm cho giá trị được lưu trong thanh ghi `rax` là giá trị được lưu ở 0x404000.

#### Lời giải

Bài này mình sẽ sử dụng các phép toán ```mov``` để gán giá trị được lưu tại địa chỉ `0x404000` cho thanh ghi `rax`:
- mov rax, [0x404000]

```python
import pwn

pwn.context.update(arch="amd64")
output = pwn.process("/challenge/run")

asm = """
    mov rax, [0x404000]
"""

output.write(pwn.asm(asm))
print(output.readallS())
```

---

#### Flag
```pwn.college{U9ghurLUvBHkvHZwkbOLTVSNVwB.QXyEDOzwCMxADNwEzW}```

---

### Level 13 - memory-write

---

#### Tóm tắt đề bài

Bây giờ chúng ta sẽ set vài giá trị trong memory trước ghi run. Mỗi lần chay, các giá trị đó sẽ thay đổi. Điều này có nghĩa là bạn cần thực hiện các thao tác theo công thức cùng với thanh ghi. Chúng tôi sẽ nói cho bạn thanh ghi nào sẽ được thiết lập trước đó và bạn nên thêm nó vào kết quả. Trong hầu hết các trường hợp, đó là `rax`.

Đối với cấp độ này, bạn sẽ làm việc với menory. Điều sẽ sẽ yêu cầu bạn đọc và ghi dữ liệu tuyến tính trong memory. Nếu bạn còn bối rối, hãy thử nhìn vào địa chỉ tuyến tính. Bạn cũng có thể yêu cầu hủy tham chiếu nhiều lần đến những thứ chúng tôi lưu vào bộ nhớ để bạn sử dụng.

Nhiệm vụ của bài:

    Đặt giá trị được lưu ở `rax` vào địa chỉ `0x404000`

---

#### Lời giải

Bài này mình sẽ sử dụng các phép toán ```mov``` để gán giá trị được lưu tại thanh ghi `rax` cho địa chỉ `0x404000`:
- `mov [0x404000], rax`

```python
import pwn

pwn.context.update(arch="amd64")
output = pwn.process("/challenge/run")

asm = """
    mov [0x404000], rax
"""

output.write(pwn.asm(asm))
print(output.readallS())
```

---

#### Flag
```pwn.college{c1FyJ-As1E4rlyCi-VxBMdJiF2p.QXzEDOzwCMxADNwEzW}```

---

### Level 14 - memory-increment

---

#### Tóm tắt đề bài

Bây giờ chúng ta sẽ set vài giá trị trong memory trước ghi run. Mỗi lần chay, các giá trị đó sẽ thay đổi. Điều này có nghĩa là bạn cần thực hiện các thao tác theo công thức cùng với thanh ghi. Chúng tôi sẽ nói cho bạn thanh ghi nào sẽ được thiết lập trước đó và bạn nên thêm nó vào kết quả. Trong hầu hết các trường hợp, đó là `rax`.

Đối với cấp độ này, bạn sẽ làm việc với menory. Điều sẽ sẽ yêu cầu bạn đọc và ghi dữ liệu tuyến tính trong memory. Nếu bạn còn bối rối, hãy thử nhìn vào địa chỉ tuyến tính. Bạn cũng có thể yêu cầu hủy tham chiếu nhiều lần đến những thứ chúng tôi lưu vào bộ nhớ để bạn sử dụng.

Nhiệm vụ của bài:
- Đặt giá trị được lưu ở địa chỉ `0x404000` vào thanh ghi `rax`.
- Tăng giá trị được lưu ở địa chỉ `0x404000` lên `0x1337`.

Chắc chắn rằng giá trị được lưu ở thanh ghi `rax` là giá trị được lưu tại địa chỉ `0x404000` và [`0x404000`] bây giờ sẽ tăng lên.

---

#### Lời giải

Bài này mình sẽ sử dụng các phép toán ```mov``` và ```add``` để gán giá trị được lưu tại thanh ghi `rax`, và tăng giá trị được lưu tại địa chỉ `0x404000` lên `0x1337`:
- `mov rax, [0x404000]`
- `mov rbx, 0x1337`
- `add [0x404000], rbx`

```python
import pwn

pwn.context.update(arch="amd64")
output = pwn.process("/challenge/run")

asm = """
    mov rax, [0x404000]
    mov rbx, 0x1337
    add [0x404000], rbx
"""

output.write(pwn.asm(asm))
print(output.readallS())
```

---

#### Flag
```pwn.college{I6PRTUgXJsA_KPGSKlKeupdhq_x.dNDMywCMxADNwEzW}```

---

### Level 15 - byte-access

---

#### Tóm tắt đề bài

Bây giờ chúng ta sẽ set vài giá trị trong memory trước ghi run. Mỗi lần chay, các giá trị đó sẽ thay đổi. Điều này có nghĩa là bạn cần thực hiện các thao tác theo công thức cùng với thanh ghi. Chúng tôi sẽ nói cho bạn thanh ghi nào sẽ được thiết lập trước đó và bạn nên thêm nó vào kết quả. Trong hầu hết các trường hợp, đó là `rax`.

Đối với cấp độ này, bạn sẽ làm việc với menory. Điều sẽ sẽ yêu cầu bạn đọc và ghi dữ liệu tuyến tính trong memory. Nếu bạn còn bối rối, hãy thử nhìn vào địa chỉ tuyến tính. Bạn cũng có thể yêu cầu hủy tham chiếu nhiều lần đến những thứ chúng tôi lưu vào bộ nhớ để bạn sử dụng.

Nhớ lại rằng thanh ghi trong `x86_64` có kích thước là 64 bits, nghĩa là ta có thể lưu tới 64 bits data. Tương tự, mỗi vùng nhớ có thể truy xuất tới giá trị 64-bit. Chúng ta có thể gọi 1 giá trị có 64 bits (8 bytes) là 1 quad word.

Dưới đây là bảng phân tích về tên của các kiểu dữ liệu trong memory:
- Quad Word = 8 Bytes = 64 bits
- Double Word = 4 bytes = 32 bits
- Word = 2 bytes = 16 bits
- Byte = 1 byte = 8 bits

Trong x86_64, bạn có thể truy cập vào từng kích thước này khi hủy tham chiếu 1 địa chỉ, nó chỉ giống như sử dụng thanh ghi lớn hơn hoặc nhỏ hơn truy cập:
- `mov al, [address]`  <=> truyền giá trị có kích thức là `byte` từ address sang `rax`
- `mov ax, [address]`  <=> truyền giá trị có kích thức là `word` từ address sang `rax`
- `mov eax, [address]`  <=> truyền giá trị có kích thức là `double word` từ address sang `rax`
- `mov rax, [address]`  <=> truyền giá trị có kích thức là `quad word` từ address sang `rax`

Nhớ rằng, truyền giá trị tới thanh ghi `al` không phải là xóa toàn bộ các byte ở trên.

Nhiệm vụ của bài:
- Đặt giá trị ở thanh ghi `rax` thành `0x404000`.

---

#### Lời giải

Bài này mình sẽ sử dụng các phép toán ```mov``` để gán giá trị tương ứng cho thanh ghi `rax`:
- `mov al [0x404000]`

```python
import pwn

pwn.context.update(arch="amd64")
output = pwn.process("/challenge/run")

asm = """
    mov al, [0x404000]
"""

output.write(pwn.asm(asm))
print(output.readallS())
```

---

#### Flag
```pwn.college{0HZTrwlu4QC8lzXhI3MEM4vLoZL.QX0EDOzwCMxADNwEzW}```

---

### Level 16 - memory-size-access

---

#### Tóm tắt đề bài

Bây giờ chúng ta sẽ set vài giá trị trong memory trước ghi run. Mỗi lần chay, các giá trị đó sẽ thay đổi. Điều này có nghĩa là bạn cần thực hiện các thao tác theo công thức cùng với thanh ghi. Chúng tôi sẽ nói cho bạn thanh ghi nào sẽ được thiết lập trước đó và bạn nên thêm nó vào kết quả. Trong hầu hết các trường hợp, đó là `rax`.

Đối với cấp độ này, bạn sẽ làm việc với menory. Điều sẽ sẽ yêu cầu bạn đọc và ghi dữ liệu tuyến tính trong memory. Nếu bạn còn bối rối, hãy thử nhìn vào địa chỉ tuyến tính. Bạn cũng có thể yêu cầu hủy tham chiếu nhiều lần đến những thứ chúng tôi lưu vào bộ nhớ để bạn sử dụng.

Nhớ lại rằng thanh ghi trong `x86_64` có kích thước là 64 bits, nghĩa là ta có thể lưu tới 64 bits data. Tương tự, mỗi vùng nhớ có thể truy xuất tới giá trị 64-bit. Chúng ta có thể gọi 1 giá trị có 64 bits (8 bytes) là 1 quad word.

Dưới đây là bảng phân tích về tên của các kiểu dữ liệu trong memory:
- Quad Word = 8 Bytes = 64 bits
- Double Word = 4 bytes = 32 bits
- Word = 2 bytes = 16 bits
- Byte = 1 byte = 8 bits

Trong x86_64, bạn có thể truy cập vào từng kích thước này khi hủy tham chiếu 1 địa chỉ, nó chỉ giống như sử dụng thanh ghi lớn hơn hoặc nhỏ hơn truy cập:
- `mov al, [address]`  <=> truyền giá trị có kích thức là `byte` từ address sang `rax`
- `mov ax, [address]`  <=> truyền giá trị có kích thức là `word` từ address sang `rax`
- `mov eax, [address]`  <=> truyền giá trị có kích thức là `double word` từ address sang `rax`
- `mov rax, [address]`  <=> truyền giá trị có kích thức là `quad word` từ address sang `rax`

Nhiệm vụ của bài:
- Truyền vào `rax` giá trị dạng `byte` tại địa chỉ `0x404000`
- Truyền vào `rbx` giá trị dạng `word` tại địa chỉ `0x404000`
- Truyền vào `rcx` giá trị dạng `double word` tại địa chỉ `0x404000`
- Truyền vào `rdx` giá trị dạng `quad word` tại địa chỉ `0x404000`

---

#### Lời giải

Bài này mình sẽ sử dụng các phép toán ```mov``` để gán giá trị tương ứng cho các thanh ghi `rax`, `rbx`, `rcx` và `rdx`:
-    `mov al, [0x404000]`
-    `mov bx, [0x404000]`
-    `mov ecx, [0x404000]`
-    `mov rdx, [0x404000]`
```python
import pwn

pwn.context.update(arch="amd64")
output = pwn.process("/challenge/run")

asm = """
    mov al, [0x404000]
    mov bx, [0x404000]
    mov ecx, [0x404000]
    mov rdx, [0x404000]
"""

output.write(pwn.asm(asm))
print(output.readallS())
```

---

#### Flag
```pwn.college{MLqkK8FKzqv1OZtK2Lwo86mMu6n.dRDMywCMxADNwEzW}```

---

### Level 17 - little-endian-write

---

#### Tóm tắt đề bài

Bây giờ chúng ta sẽ set vài giá trị trong memory trước ghi run. Mỗi lần chay, các giá trị đó sẽ thay đổi. Điều này có nghĩa là bạn cần thực hiện các thao tác theo công thức cùng với thanh ghi. Chúng tôi sẽ nói cho bạn thanh ghi nào sẽ được thiết lập trước đó và bạn nên thêm nó vào kết quả. Trong hầu hết các trường hợp, đó là `rax`.

Đối với cấp độ này, bạn sẽ làm việc với menory. Điều sẽ sẽ yêu cầu bạn đọc và ghi dữ liệu tuyến tính trong memory. Nếu bạn còn bối rối, hãy thử nhìn vào địa chỉ tuyến tính. Bạn cũng có thể yêu cầu hủy tham chiếu nhiều lần đến những thứ chúng tôi lưu vào bộ nhớ để bạn sử dụng.

Nó đáng chú ý và có lẽ bạn cũng đã nhận thấy, các giá trị được lưu trữ theo thứ tự ngược lại so với những gì ta biểu diễn chúng.

Có 1 ví dụ sau:

    [0x1330] = 0x00000000deadc0de

Nếu bạn thử kiếm tra thì hãy nhìn vào memory, bạn sẽ thấy như sau:

    [0x1330] = 0xde
    [0x1331] = 0xc0
    [0x1332] = 0xad
    [0x1333] = 0xde
    [0x1334] = 0x00
    [0x1335] = 0x00
    [0x1336] = 0x00
    [0x1337] = 0x00

Format dạng này lưu trữ mọi thứ theo kiểu ngược lại như này là cố ý trong x86, and nó được gọi là "Little Endian".

Đối với thử thách lần này, chúng tôi sẽ gửi cho bạn 2 địa chỉ đã được khởi tại mỗi khi run.

Địa chỉ đầu tiên sẽ được đặt tại ```rdi```, và địa chỉ thứ 2 được đặt tại ```rsi```.

Nhiệm vụ của bài:
- Đặt `[rdi] = 0xdeadbeef00001337`
- Đặt `[rsi] = 0xc0ffee0000`

Gợi ý: Nó có lẽ sẽ yêu cầu 1 vài trick đặt 1 hằng số lớn cho thanh khi không tham chiếu. Thử thiết lập một thanh ghi thành giá trị hằng số, sau đó gán thanh ghi đó cho thanh ghi không tham chiếu.

---

#### Lời giải

Bài này mình sẽ sử dụng phép toán `mov` để gán giá trị tương ứng cho 2 địa chỉ được lưu ở 2 thanh ghi `rdi` và `rsi`. Tuy nhiên, ta không thể gán trực tiếp như sau:

    mov [address], value

Vì thế mình sẽ truyền giá trị qua cho 1 thanh ghi sau đó truyền từ thanh ghi đó vào địa chỉ tương ứng đó:
-   `mov rax, 0xdeadbeef00001337`
-   `mov [rdi], rax`
-   `mov rax, 0xc0ffee0000`
-   `mov [rsi], rax`


```python
import pwn

pwn.context.update(arch="amd64")
output = pwn.process("/challenge/run")

asm = """
    mov rax, 0xdeadbeef00001337
    mov [rdi], rax
    mov rax, 0xc0ffee0000
    mov [rsi], rax
"""

output.write(pwn.asm(asm))
print(output.readallS())
```

---

#### Flag
```pwn.college{cQq3fNjzaEerE60RefQpwxg6R1u.dVDMywCMxADNwEzW}```

---

### Level 18 - memory-sum

--- 

#### Tóm tắt đề bài

Bây giờ chúng ta sẽ set vài giá trị trong memory trước ghi run. Mỗi lần chay, các giá trị đó sẽ thay đổi. Điều này có nghĩa là bạn cần thực hiện các thao tác theo công thức cùng với thanh ghi. Chúng tôi sẽ nói cho bạn thanh ghi nào sẽ được thiết lập trước đó và bạn nên thêm nó vào kết quả. Trong hầu hết các trường hợp, đó là `rax`.

Đối với cấp độ này, bạn sẽ làm việc với menory. Điều sẽ sẽ yêu cầu bạn đọc và ghi dữ liệu tuyến tính trong memory. Nếu bạn còn bối rối, hãy thử nhìn vào địa chỉ tuyến tính. Bạn cũng có thể yêu cầu hủy tham chiếu nhiều lần đến những thứ chúng tôi lưu vào bộ nhớ để bạn sử dụng.

Nhớ lạy rằng memory được lưu theo đường thẳng.

Điều này có nghĩa là gì?
Chúng ta có thể truy cập vào địa chỉ `0x1337`:

    [0x1337] = 0x00000000deadbeef

Cách bố trí bộ nhớ thực sự là theo từng byte, `little endian`:

    [0x1337] = 0xef
    [0x1337 + 1] = 0xbe
    [0x1337 + 2] = 0xad
    ...
    [0x1337 + 7] = 0x00

Điều này có tác dụng gì với chúng ta?
Well, nó có nghĩa là chúng ta có thể truy cập vào những thứ nằm cạnh nhau bằng cách sử dụng offsets, giống như những gì đã show ở trên.

Giả sử bạn muốn byte thứ 5 từ 1 địa chỉ, bạn có thể thử truy cập như sau:
   
    mov al, [address+4]

Nhắc lại, offsets bắt đầu từ 0.

Nhiệm vụ của bài:
- Load 2 giá trị liên tiếp có kích thước quad words từ địa chỉ được lưu ở `rdi`.
- Thực hiện tính tổng giá trị từ bước trước.
- Lưu tổng tại địa chỉ được lưu ở `rdi`

--- 

#### Lời giải

Bài này mình sẽ sử dụng các toán tử như `mov` và `add` để tính toán các giá trị phù hợp được lưu tại các địa chỉ và các thanh ghi:

-   `mov rax, [rdi]`
-   `mov rbx, [rdi + 8]`
-   `add rax, rbx`
-   `mov [rsi], rax`


```python
import pwn

pwn.context.update(arch="amd64")
output = pwn.process("/challenge/run")

asm = """
    mov rax, [rdi]
    mov rbx, [rdi + 8]
    add rax, rbx
    mov [rsi], rax
"""

output.write(pwn.asm(asm))
print(output.readallS())
```

---

#### Flag
```pwn.college{4eaKS2EFr1rHQEQAFLZlqCP-mm4.dZDMywCMxADNwEzW}```

---

### Level 19 - stack-subtraction

---

#### Tóm tắt đề bài

Bây giờ chúng ta sẽ set vài giá trị trong memory trước ghi run. Mỗi lần chay, các giá trị đó sẽ thay đổi. Điều này có nghĩa là bạn cần thực hiện các thao tác theo công thức cùng với thanh ghi. Chúng tôi sẽ nói cho bạn thanh ghi nào sẽ được thiết lập trước đó và bạn nên thêm nó vào kết quả. Trong hầu hết các trường hợp, đó là `rax`.

Trong cấp độ này, bạn sẽ làm việc với stack, vùng nhớ sẽ có khả năng mở rộng và co lại 1 cách linh hoạt. Bạn sẽ được yêu cầu đọc và ghi vào stack, nó yêu cầu bạn sẽ sử dụng `pop` và `push`. Có lẽ bạn cũng sẽ cần sử dụng thanh ghi con trỏ ngăn xếp (pointer register -> `rsp`) được hiểu là con trỏ của ngăn xếp.

Trong những cấp độ này, chúng ta sẽ cùng giới thiệu về stack.

Stack là 1 vùng của bộ nhớ có thể lưu giá trị để sử dụng sau.

Khi mà lưu giá trị vào stack, chúng ta có thể sử dụng lệnh `push`, và nếu muốn trả về 1 phần tử thì chúng ta có thể sử dụng lệnh `pop`.

Vùng nhớ stack được tổ chức theo cấu trúc vào trước ra sau(LIFO), và điều này có nghĩa là giá trị cuối cùng được thêm vào là giá trị đầu tiêu được bỏ qua.

Tưởng tượng việc dỡ dĩa ra khỏi máy rửa chén. Giả sử có 1 quả đỏ, 1 quả xanh lá cây và 1 quả xanh dương. Đầu tiên, ta đặt quả đỏ vào tủ, sau đó đặt quả xanh lá cây lên trên quả đỏ, rồi đến quả xanh dương.

Chồng dĩa của chúng ta sẽ được trong như thế này:

    Top ----> Blue
              Green
    Bottom -> Red

Bây giờ, nếu chúng ta muốn 1 cái dĩa để làm bánh sandwich, chúng ta sẽ trả về cái dĩa trên cùng của stack, vì nó là chiếc dĩa cuối cùng được vào trong tủ, nên nó là chiếc dĩa đầu tiên được lấy ra.

Trong x86, lệnh `pop` sẽ lấy giá trị từ đỉnh của stack và lưu vào 1 thanh ghi nào đó.

Tương tự, lệnh `push` sẽ lấy giá trị ở trong 1 thanh ghi và thêm vào trên đỉnh của stack.

Sử dụng những lệnh trên.

Nhiệm vụ của bài:
- Lấy giá trị trên cùng của stack
- Sau đó đem trừ cho `rdi`
- Và cuối cùng là thêm lại vào đỉnh của stack

--- 

#### Lời giải

Bài này mình sẽ sử dụng các lệnh được nêu ở trên đó là `pop` và `push` để có thể tương tác với stack:

-   `pop rax`
-   `sub rax, rdi`
-   `push rax`


```python
import pwn

pwn.context.update(arch="amd64")
output = pwn.process("/challenge/run")

asm = """
    pop rax
    sub rax, rdi
    push rax
"""

output.write(pwn.asm(asm))
print(output.readallS())
```

---

#### Flag
```pwn.college{0bMhlV53LjYtukPepUva60WVjdI.ddDMywCMxADNwEzW}```

---

### Level 20 - swap-stack-values

---

#### Tóm tắt đề bài

Bây giờ chúng ta sẽ set vài giá trị trong memory trước ghi run. Mỗi lần chay, các giá trị đó sẽ thay đổi. Điều này có nghĩa là bạn cần thực hiện các thao tác theo công thức cùng với thanh ghi. Chúng tôi sẽ nói cho bạn thanh ghi nào sẽ được thiết lập trước đó và bạn nên thêm nó vào kết quả. Trong hầu hết các trường hợp, đó là `rax`.

Trong cấp độ này, bạn sẽ làm việc với `stack`, vùng nhớ sẽ có khả năng mở rộng và co lại 1 cách linh hoạt. Bạn sẽ được yêu cầu đọc và ghi vào `stack`, nó yêu cầu bạn sẽ sử dụng `pop` và `push`. Có lẽ bạn cũng sẽ cần sử dụng thanh ghi con trỏ ngăn xếp (pointer register -> `rsp`) được hiểu là con trỏ của ngăn xếp.

Đối với cấp độ này, chúng ta sẽ khám phá cấu trúc vào trước ra sau trong `stack`.

Chỉ sử dụng các lệnh sau:
- `push`
- `pop`

Nhiệm cụ của bài:

    Đối chổ 2 giá trị ở `rdi` và `rsi`.

    Ví dụ:
    - Nếu ban đầu tại rdi = 2 và rsi = 5
    - Thì lúc kết thúc rdi = 5, và rsi = 2`

---

#### Lời giải

Bài này mình sẽ sử dụng các lệnh được nêu ở trên đó là `pop` và `push` để có thể tương tác với stack:

-   `push rdi`
-   `push rsi`
-   `pop rdi`
-   `pop rsi`


```python
import pwn

pwn.context.update(arch="amd64")
output = pwn.process("/challenge/run")

asm = """
    push rdi
    push rsi
    pop rdi
    pop rsi
"""

output.write(pwn.asm(asm))
print(output.readallS())
```

---

#### Flag
```pwn.college{Ax8XdJMcTntp3jk_mSam_VfEkx1.dhDMywCMxADNwEzW}```

---

### Level 21 - average-stack-values

---

#### Tóm tắt đề bài

Bây giờ chúng ta sẽ set vài giá trị trong memory trước ghi run. Mỗi lần chay, các giá trị đó sẽ thay đổi. Điều này có nghĩa là bạn cần thực hiện các thao tác theo công thức cùng với thanh ghi. Chúng tôi sẽ nói cho bạn thanh ghi nào sẽ được thiết lập trước đó và bạn nên thêm nó vào kết quả. Trong hầu hết các trường hợp, đó là `rax`.

Trong cấp độ này, bạn sẽ làm việc với `stack`, vùng nhớ sẽ có khả năng mở rộng và co lại 1 cách linh hoạt. Bạn sẽ được yêu cầu đọc và ghi vào `stack`, nó yêu cầu bạn sẽ sử dụng `pop` và `push`. Có lẽ bạn cũng sẽ cần sử dụng thanh ghi con trỏ ngăn xếp (pointer register -> `rsp`) được hiểu là con trỏ của ngăn xếp.

Trong cấp độ trước, bạn đã sử dụng `push` và `pop` để lưu và load dữ liệu từ stack. Tuy nhiên, bạn cũng có thể truy cập trực tiếp vào stack bằng cách sử dụng con trỏ ngăn xếp.

Trong x86, địa chỉ ngăn xếp được lưu trong thanh ghi đặc biệt (`rsp`). `rsp` thường lưu trữ địa chỉ bộ nhớ của đỉnh stack. Là địa chỉ của phần tử được thêm vào cuối stack.

Tương tự như các cấp độ trước, chúng ta có thể sử dụng `[rsp]` để truy cập vào giá trị được lưu tại địa chỉ trong `rsp`.

Nhiệm vụ của bài:
- Không sử dụng `pop`, hãy tính toán giá trị trung bình của các phần tử có kiểu dữ liệu `quad word` được lưu liên tiếp trên stack. Thêm giá trị trung bình vào stack.
- Hint:
    - RSP+0x?? Quad Word A
    - RSP+0x?? Quad Word B
    - RSP+0x?? Quad Word C
    - RSP Quad Word D

---

#### Lời giải

Bài này mình truy cập trực tiếp vào các địa chỉ liên tiếp và bắt đầu là địa chỉ được lưu tại thanh ghi `rsp`, sau đó mình sẽ tính giá trị trung bình và đẩy lên `stack`:

-    `mov rax, [rsp]`
-    `add rax, [rsp + 8]`
-    `add rax, [rsp + 16]`
-    `add rax, [rsp + 24]`
-    `mov rbx, 0x4`
-    `div rbx`
-    `push rax`


```python
import pwn

pwn.context.update(arch="amd64")
output = pwn.process("/challenge/run")

asm = """
    mov rax, [rsp]
    add rax, [rsp + 8]
    add rax, [rsp + 16]
    add rax, [rsp + 24]
    mov rbx, 0x4
    div rbx
    push rax
"""

output.write(pwn.asm(asm))
print(output.readallS())
```

---

#### Flag
```pwn.college{IBbMl_zp-x6AkWRvgllLkw7QUdE.dlDMywCMxADNwEzW}```

---

### Level 22 - absolute-jump

--- 

#### Tóm tắt đề bài

Bây giờ chúng ta sẽ set vài giá trị trong memory trước ghi run. Mỗi lần chay, các giá trị đó sẽ thay đổi. Điều này có nghĩa là bạn cần thực hiện các thao tác theo công thức cùng với thanh ghi. Chúng tôi sẽ nói cho bạn thanh ghi nào sẽ được thiết lập trước đó và bạn nên thêm nó vào kết quả. Trong hầu hết các trường hợp, đó là `rax`.

Trong cấp độ này, bạn sẽ được làm việc với kiểm soát thao tác luồng. Điều này liên quan đến việc sử dụng các hướng dẫn gián tiếp hoặc trực tiếp để điều khiển các thanh ghi đặc biệt `rip`, con trỏ lệnh. Bạn sẽ sử dụng các lệnh như `jmp`, `call`, `cmp`, và 1 số lựa chọn thay thế việc thực hiện các yêu cầu hành vi. 

Trước đó, bạn đã học về làm cách nào để thao tác data trong `pseudo-control` (kiểm soát giả), nhưng x86 thực sự cung cấp các hướng dẫn cho bạn kiểm soát luồng trực tiếp.

Có 2 cách chính để điều khiển luồng điều khiển:
- Gọi lệnh `jump`
- Gọi lệnh `call`

Trong cấp độ này, bạn sẽ làm việc với jumps.

Có 2 loại jumps.
- jumps có điều kiện
- jumps không có điều kiện

Jumps không có điều kiện luôn được kích hoạt và không dựa trên kết quả của các lệnh trước đó.

Như bạn đã biết, vùng nhớ có thể lưu data và các instructions. Code của bạn sẽ được lưu tại `0x400042` (điều này sẽ thay đổi mỗi khi chạy).

Trong tất cả các jumps, có 3 loại như sau:
- Nhảy tương đối (relative jumps): jump + or - next instruction.
- Nhảy tuyệt đối (absolute jumps): nhảy tới địa chỉ cụ thể
- Nhảy gián tiếp (indirect jumps): nhảy tới địa chỉ cụ thể trong thanh ghi.

Trong x86, lệnh nhảy tuyệt đối (nhảy đến một địa chỉ cụ thể) được thực hiện bằng cách đầu tiên tải địa chỉ đích vào một thanh ghi mục đích chung (chúng ta sẽ gọi thanh ghi giữ chỗ này là `reg`), sau đó thực hiện lệnh `jmp reg`.

Trong cấp độ này, chúng tôi sẽ yêu cầu bạn thực hiện 1 lệnh nhảy tuyệt đối. 

Nhiệm vụ của bài:
- Nhảy tới địa chỉ tuyệt đối: `0x403000`.

---

#### Lời giải

Bài này mình sẽ truyền địa chỉ để nhảy vào 1 thanh ghi, sau đó jumps tới thanh ghi đó:

-   `mov rax, 0x403000`
-   `jmp rax`


```python
import pwn

pwn.context.update(arch="amd64")
output = pwn.process("/challenge/run")

asm = """
    mov rax, 0x403000
    jmp rax
"""

output.write(pwn.asm(asm))
print(output.readallS())
```

---

#### Flag
```pwn.college{Yrzc6mRCx6gt0MwNMsDezmAp_qv.QX1EDOzwCMxADNwEzW}```

---

### Level 23 - relative-jump

---

#### Tóm tắt đề bài

Bây giờ chúng ta sẽ set vài giá trị trong memory trước ghi run. Mỗi lần chay, các giá trị đó sẽ thay đổi. Điều này có nghĩa là bạn cần thực hiện các thao tác theo công thức cùng với thanh ghi. Chúng tôi sẽ nói cho bạn thanh ghi nào sẽ được thiết lập trước đó và bạn nên thêm nó vào kết quả. Trong hầu hết các trường hợp, đó là `rax`.

Trong cấp độ này, bạn sẽ được làm việc với kiểm soát thao tác luồng. Điều này liên quan đến việc sử dụng các hướng dẫn gián tiếp hoặc trực tiếp để điều khiển các thanh ghi đặc biệt `rip`, con trỏ lệnh. Bạn sẽ sử dụng các lệnh như `jmp`, `call`, `cmp`, và 1 số lựa chọn thay thế việc thực hiện các yêu cầu hành vi. 

Nhớ lại rằng trong tất cả các jumps, có 3 loại như sau:
- Nhảy tương đối (relative jumps)
- Nhảy tuyệt đối (absolute jumps)
- Nhảy gián tiếp (indirect jumps)

Trong cấp độ này, chúng tôi sẽ yêu cầu bạn thực hiện 1 lệnh nhảy tương đối. Bạn sẽ cần điền 1 khoảng trống trong code của bạn để thực hiện có nhảy tương đối này. Chúng tôi gợi ý sử dụng lệnh `nop`. Nó dài 1 byte và rất dễ đoán.

Trong thực tế, trình biên dịch của chúng tôi có sử dụng 1 tiện ích, `.rept` nói rằng bạn có thể lặp lại lệnh assembly 1 số lần. 

Các lệnh hữu ích cho cấp độ này:
- `jmp`, `(reg1 | addr | offset)`   
- `nop`

Gợi ý: Trong nhảy tương đối, hãy tìm hiểu cách sử dụng `x86`. 

Sử dụng những kiến thức ở trên, nhiệm vụ của bài:
- Đặt lệnh đầu tiên trong code của bạn là `jmp`.
- Đặt lệnh `jmp` tương đối tới `0x51` bytes  từ vị trí hiện tại.
- Tại vị trí code ở đây là tương đối sẽ chuyển hưởng luồng điều khiển, đặt `rax` thành `0x1`.

---

#### Lời giải

Bài này mình sẽ sử dụng lệnh `.rept` và `nop` để tạo ra một khoảng code với kích thước `0x51`. Sau đó mình sẽ tạo ra 1 label và jump tới label đó.

-   `jmp rlt`
-   `.rept 0x51`
-   `    nop`
-   `.endr`
-   `rlt:`
-   `    mov rax, 0x1`

```python
import pwn

pwn.context.update(arch="amd64")
output = pwn.process("/challenge/run")

asm = """
    jmp rlt
    .rept 0x51
    nop
    .endrz
    rlt:
    mov rax, 0x1
"""

output.write(pwn.asm(asm))
print(output.readallS())
```

---

#### Flag
```pwn.college{gZIbnSCceZgFosyEjrEKENNK5Ra.QX2EDOzwCMxADNwEzW}```

---

### Level 24 - jump-trampoline

---

#### Tóm tắt đề bài

Bây giờ chúng ta sẽ set vài giá trị trong memory trước ghi run. Mỗi lần chay, các giá trị đó sẽ thay đổi. Điều này có nghĩa là bạn cần thực hiện các thao tác theo công thức cùng với thanh ghi. Chúng tôi sẽ nói cho bạn thanh ghi nào sẽ được thiết lập trước đó và bạn nên thêm nó vào kết quả. Trong hầu hết các trường hợp, đó là `rax`.

Trong cấp độ này, bạn sẽ được làm việc với kiểm soát thao tác luồng. Điều này liên quan đến việc sử dụng các hướng dẫn gián tiếp hoặc trực tiếp để điều khiển các thanh ghi đặc biệt `rip`, con trỏ lệnh. Bạn sẽ sử dụng các lệnh như `jmp`, `call`, `cmp`, và 1 số lựa chọn thay thế việc thực hiện các yêu cầu hành vi. 

Bây giờ, chúng tôi sẽ gộp 2 level trước lại

Nhiệm vụ của bài:

- Tạo 2 lệnh nhảy:
    - Đặt lệnh đầu tiên trong code của bạn là `jmp`.
    - Đặt lệnh `jmp` tương đối tới `0x51` bytes  từ vị trí hiện tại.
    - Tại 0x51, thực hiện theo yêu cầu sau:
        - Đặt giá trị trên đỉnh của stack vào thanh ghi `rdi`.
        - Sử dụng `jmp` để thực hiện nhảy tuyệt đối tới địa chỉ 0x403000.

---

#### Lời giải

Bài này mình sẽ kết hợp các lệnh 2 cấp độ trước lại để có thể thực hiện yêu cầu của bài. Đầu tiên mình sẽ sử dụng lệnh `.rept` và `nop` để tạo ra một khoảng code với kích thước `0x51`. Sau đó mình sẽ tạo ra 1 label và jump tới label đó. Trong label đó mình sẽ đặt giá trị trên đỉnh của stack vào thanh ghi `rdi` và nhảy tới địa chỉ `0x403000`.

-   `jmp rlt`
-   `.rept 0x51`
-   `nop`
-   `.endr`
-   `rlt:`
-   `pop rdi`
-   `mov rbx, 0x403000`
-   `jmp rbx`

```python
import pwn

pwn.context.update(arch="amd64")
output = pwn.process("/challenge/run")

asm = """
    jmp rlt
    .rept 0x51
        nop
    .endr
    rlt:
        pop rdi
        mov rbx, 0x403000
        jmp rbx
"""

output.write(pwn.asm(asm))
print(output.readallS())
```

---

#### Flag
```pwn.college{YmmK3ctHyLYm1CMhKmN3aUJeJsi.dBTMywCMxADNwEzW}```

---

### Level 25 - conditional-jump

---

#### Tóm tắt đề bài

Trong cấp độ này, bạn sẽ được làm việc với kiểm soát thao tác luồng. Điều này liên quan đến việc sử dụng các hướng dẫn gián tiếp hoặc trực tiếp để điều khiển các thanh ghi đặc biệt `rip`, con trỏ lệnh. Bạn sẽ sử dụng các lệnh như `jmp`, `call`, `cmp`, và 1 số lựa chọn thay thế việc thực hiện các yêu cầu hành vi. 

Chúng tôi sẽ kiểm tra mã của bạn nhiều lần trong thử thách lần này! Điều này có nghĩa là chúng tôi sẽ chạy code của bạn kết hợp với giá trị random trong mỗi lần chạy để đảm bảo rằng login của bạn đúng để đủ sử dụng trong điều kiện sử dụng bình thường.

Chúng tôi sẽ giới thiệu cho bạn về nhảy nhưng có điều kiện. Một trong những lệnh có giá trị nhất trong x86. Trong ngôn ngữ bậc cao, lệnh if-else được tổ chức kiểu như sau:

    if x is even:
        is_even = 1
    else:
        is_even = 0

Điều này nhìn nó rất quen thuộc vì có thể sử dụng bit-logic, điều mà bạn đã thực hiện ở cấp độ trước. Trong những cấu trúc này, bạn có thể kiểm soát chương trình điều khiển luồng thực thi vào những giá trị động cung cấp cho chương trình.

Thực thi các logic ở trên cùng với jmps có thể trong như sau:

    ; assume rdi = x, rax is output
    ; rdx = rdi mod 2
    mov rax, rdi
    mov rsi, 2
    div rsi
    ; remainder is 0 if even
    cmp rdx, 0
    ; jump to not_even code if it's not 0
    jne not_even
    ; fall through to even code
    mov rbx, 1
    jmp done
    ; jump to this only when not_even
    not_even:
    mov rbx, 0
    done:
    mov rax, rbx
    ; more instructions here

Tuy nhiên, bạn muốn nhiều hơn chứ không chỉ mỗi `if-else`. Đôi khi bạn muốn sử dụng 2 câu lệnh if, theo sau là `else`. Để làm được điều đó, bạn cần chắc chắn rằng bạn đã có luồng điều khiển qua 'falls-though` nếu nó bị lỗi. Tất cả phải nhảy đến 1 thực hiện để trách người dùng khác.

Có rất nhiều dạng jumps trong x86, sẽ rất hữu ích khi chúng ta học cách sử dụng. Gần như tất cả đều dựa vào những thứ được gọi là ZF,  Zero Flag. ZF sẽ được set thành 1 khi chúng ta thực hiện so sách và cho ra kết quả là bằng nhau, và 0 với trường hợp còn lại.

Sử dụng những kiến thức được cho ở trên.

Nhiệm vụ của bài:

    if [x] is 0x7f454c46:
        y = [x+4] + [x+8] + [x+12]
    else if [x] is 0x00005A4D:
        y = [x+4] - [x+8] - [x+12]
    else:
        y = [x+4] * [x+8] * [x+12]

Ở đây:
- x = edi, y = eax.

Cho rằng mỗi giá trị hủy tham chiếu là giá trị dword đơn lẻ. Điều này có nghĩa là giá trị có thể bắt đầu bằng một giá trị âm trong mỗi vùng nhớ.

Một giải pháp hợp lệ sẽ sử dụng các lệnh được cho như sau ít nhất 1 lần:
-   `jmp`, `cmp`    

---

#### Lời giải

Bài này có 3 trường hợp, nên mình sẽ viết từng label cho từng trường hợp đó. Ban đầu mình sẽ viết label đầu cho trường hợp đầu tiên, tiếp theo nếu trong label đó mà so sách không khớp thì nó sẽ nhảy sang label thứ 2, và tiếp tục nếu không khớp nữa thì sẽ nhảy vào label cuối cùng và thực hiện ở đây mà không so sánh nữa. Trong mỗi label sau khi so sánh hợp lệ và thực hiện hết mình sẽ nhảy tới label done.

```python
import pwn

pwn.context.update(arch="amd64")
output = pwn.process("/challenge/run")

asm = """
    jmp .check1

    .check1:
        cmp dword ptr [edi], 0x7f454c46
        jne .check2

        mov eax, dword ptr [rdi + 0x4]
        add eax, dword ptr [rdi + 0x8]
        add eax, dword ptr [rdi + 0xc]
        
        jmp .done

    .check2:
        cmp dword ptr [edi], 0x00005A4D
        jne .else

        mov eax, dword ptr [rdi + 0x4]
        sub eax, dword ptr [rdi + 0x8]
        sub eax, dword ptr [rdi + 0xc]

        jmp .done

    .else:
        mov eax, dword ptr [rdi + 0x4]
        imul eax, dword ptr [rdi + 0x8]
        imul eax, dword ptr [rdi + 0xc]

        jmp .done

    .done:
        nop
"""

output.write(pwn.asm(asm))
print(output.readallS())
```

---

#### Flag
```pwn.college{sd2RjHgda2tWZDtMJYG-U7jB3M1.dFTMywCMxADNwEzW}```

---

### Level 26 - indicrect-jump

---

#### Tóm tắt đề bài

Trong cấp độ này, bạn sẽ được làm việc với kiểm soát thao tác luồng. Điều này liên quan đến việc sử dụng các hướng dẫn gián tiếp hoặc trực tiếp để điều khiển các thanh ghi đặc biệt `rip`, con trỏ lệnh. Bạn sẽ sử dụng các lệnh như `jmp`, `call`, `cmp`, và 1 số lựa chọn thay thế việc thực hiện các yêu cầu hành vi. 

Chúng tôi sẽ kiểm tra mã của bạn nhiều lần trong thử thách lần này! Điều này có nghĩa là chúng tôi sẽ chạy code của bạn kết hợp với giá trị random trong mỗi lần chạy để đảm bảo rằng login của bạn đúng để đủ sử dụng trong điều kiện sử dụng bình thường.

Loại nhảy cuối cùng là nhảy gián tiếp (indirect jump), thường được dùng cho câu lệnh `switch` trong lập trình thực tế. Câu lệnh `switch` là một dạng đặc biệt của cấu trúc if-else, nhưng chỉ sử dụng số để xác định luồng điều khiển sẽ đi đâu.

Ví dụ:  

    switch(number):
    0: jmp do_thing_0
    1: jmp do_thing_1
    2: jmp do_thing_2
    default: jmp do_default_thing

Trong ví dụ này, `switch` hoạt động trên biến `number`, có thể là 0, 1 hoặc 2. Nếu `number` không nằm trong các giá trị đó, lệnh mặc định sẽ chạy. Bạn có thể coi đây là một phiên bản rút gọn của cấu trúc `else-if`. Trong x86, vì ta thường xuyên làm việc với số, nên không ngạc nhiên khi có thể đưa ra quyết định dựa trên giá trị cụ thể. Nếu biết rõ phạm vi của các số, câu lệnh switch hoạt động rất hiệu quả.

Ví dụ: một jump table là một vùng bộ nhớ liên tiếp lưu các địa chỉ cần nhảy tới.

Bảng nhảy có thể trông như sau:

    [0x1337]      = địa chỉ do_thing_0
    [0x1337+0x8]  = địa chỉ do_thing_1
    [0x1337+0x10] = địa chỉ do_thing_2
    [0x1337+0x18] = địa chỉ do_default_thing

Khi đó, thay vì nhiều lệnh cmp, ta chỉ cần kiểm tra xem number có lớn hơn 2 không. Nếu lớn hơn, luôn nhảy đến:
- `jmp [0x1337+0x18]`

Ngược lại:
- `jmp [jump_table_address + number * 8]`

Nhiệm vụ của bài:

    if rdi == 0:
        jmp 0x40301e
    else if rdi == 1:
        jmp 0x4030da
    else if rdi == 2:
        jmp 0x4031d5
    else if rdi == 3:
        jmp 0x403286
    else:
        jmp 0x4932c

Ràng buộc

- Giả sử rdi sẽ không âm.
-   Không dùng quá 1 lệnh cmp.
-   Không dùng quá 3 lệnh jmp (mọi loại).
-   Chúng tôi sẽ cung cấp số để switch trong rdi.
-   Chúng tôi cũng sẽ cung cấp địa chỉ cơ sở của jump table trong rsi.

Ví dụ cho 1 bảng:

    [0x40427c] = 0x40301e
    [0x404284] = 0x4030da
    [0x40428c] = 0x4031d5
    [0x404294] = 0x403286

--- 

#### Lời giải:
Bài này ban đầu mình sẽ so sánh rdi với 3, và nếu rdi nhỏ hơn hoặc bằng 3
thì mình sẽ nhảy đến `[8 * rdi + rsi]`.

```python
import pwn

pwn.context.update(arch="amd64")
output = pwn.process("/challenge/run")

asm = """
    cmp rdi, 0x3
    jbe .else
    mov rdi, 4

    .else:
        mov rax, [rdi * 8 + rsi]
        jmp rax
"""

output.write(pwn.asm(asm))
print(output.readallS())
```

---

#### Flag
```pwn.college{cVHVmKjaKUTcS6XbGBrIHC2zQ3b.dJTMywCMxADNwEzW}```

---

### Level 27 - average-loop

---

#### Tóm tắt đề bài

Chúng ta sẽ thiết lập một số giá trị trong bộ nhớ `động` trước mỗi lần chạy. Ở mỗi lần chạy, các giá trị sẽ thay đổi. Điều này có nghĩa là bạn sẽ cần thực hiện một số phép toán công thức với các thanh ghi. Chúng tôi sẽ cho bạn biết thanh ghi nào được thiết lập trước và bạn nên đặt kết quả ở đâu. Trong hầu hết các trường hợp, kết quả sẽ nằm trong `rax`.

Ở cấp độ này, bạn sẽ làm việc với `điều khiển luồng (control flow manipulation)`. Điều này bao gồm việc sử dụng các lệnh để gián tiếp và trực tiếp điều khiển thanh ghi đặc biệt `rip` (instruction pointer). Bạn sẽ sử dụng các lệnh như `jmp, call, cmp` và các biến thể của chúng để triển khai hành vi được yêu cầu.

Trong một cấp trước đó, bạn đã tính trung bình của 4 số nguyên (quad words), đây là một lượng cố định để tính toán. Nhưng làm thế nào để xử lý với những kích thước được cung cấp `khi chương trình đang chạy`?

Trong hầu hết các ngôn ngữ lập trình, có một cấu trúc gọi là `for-loop`, cho phép bạn thực thi một tập hợp lệnh trong một khoảng số lần xác định. Số lần lặp có thể đã được biết trước hoặc được cung cấp động khi chương trình chạy.

Ví dụ, một vòng lặp for có thể được dùng để tính tổng các số từ 1 đến n:
 
    sum = 0
    i = 1
    while i <= n:
        sum += i
        i += 1

Nhiệm vụ của bài:

- Hãy tính trung bình của n quad words liên tiếp, trong đó:

    - **rdi** = địa chỉ bộ nhớ của quad word đầu tiên  
    - **rsi** = n (số lượng cần lặp)  
    - **rax** = giá trị trung bình đã tính  

---

#### Lời giải:
Bài này ban đầu mình sẽ khởi tạo giá trị ban đầu cho `sum` và `i` được lưu tương ứng ở `rcx` và `rdx`. Sau đó mình sẽ viết 2 label để có thể hoạt động như vòng lặp và tính toán yêu cầu của bài.

```python
import pwn

pwn.context.update(arch="amd64")
output = pwn.process("/challenge/run")

asm = """
    mov rcx, [rdi]
    mov rdx, 0x1

    jmp .loop

    .loop:
        cmp rdx, rsi
        jg .endloop

        add rcx, [rdi + rdx * 0x8]
        add rdx, 0x1

        jmp .loop

    .endloop:
        xor rdx, rdx    #rdx:rax / rsi -> clear rdx
        mov rax, rcx
        div rsi

"""

output.write(pwn.asm(asm))
print(output.readallS())
```

---

#### Flag
```pwn.college{oPkY2SJxYehy1jmf8co-mDyDm40.dNTMywCMxADNwEzW}```

---

### Level 28 - count-non-zero

---

#### Tóm tắt đề bài

Trong level này, bạn sẽ làm việc với việc thao tác luồng điều khiển. Điều này liên quan đến việc sử dụng các lệnh để gián tiếp và trực tiếp điều khiển thanh ghi đặc biệt `rip`, tức con trỏ lệnh. Bạn sẽ sử dụng các lệnh như `jmp`, `call`, `cmp`, và các biến thể của chúng để thực hiện hành vi được yêu cầu.

Chúng tôi sẽ kiểm tra code của bạn nhiều lần trong level này với các giá trị động. Điều này có nghĩa là chúng tôi sẽ chạy code của bạn với nhiều cách ngẫu nhiên để kiểm tra xem logic có đủ mạnh để hoạt động ổn định không.

Ở các level trước, bạn đã khám phá vòng lặp `for` để lặp lại một số lần, có thể là động hoặc tĩnh. Nhưng nếu bạn muốn lặp cho đến khi gặp một điều kiện thì sao?  

Có một cấu trúc vòng lặp thứ hai gọi là `while-loop` để đáp ứng nhu cầu này. Trong `while-loop`, bạn lặp lại cho đến khi một điều kiện được thỏa mãn.

Ví dụ:

- Giả sử chúng ta có một vùng nhớ với các số liền kề và chúng ta muốn lấy trung bình của tất cả các số cho đến khi gặp một số lớn hơn hoặc bằng `0xff`:

        average = 0
        i = 0
        while x[i] < 0xff:
            average += x[i]
            i += 1
        average /= i

Dựa trên kiến thức trên, hãy thực hiện như sau:

Đếm số byte liên tiếp khác 0 trong một vùng nhớ liên tục, với:
- `rdi` = địa chỉ ô nhớ của byte đầu tiên
- `rax` = số byte liên tiếp khác 0

Ngoài ra, nếu rdi = 0 thì set rax = 0 (chúng tôi sẽ kiểm tra điều này)!

Và ví dụ có 1 testcase như sau:

- `rdi = 0x1000`
- `[0x1000] = 0x41`
- `[0x1001] = 0x42`
- `[0x1002] = 0x43`
- `[0x1003] = 0x00`

Sau đó: `rax = 3` sẽ được set

---

#### Lời giải:
Bài này ban đầu mình sẽ khởi tạo giá trị ban đầu cho biến đếm (`rax`). Sau đó mình sẽ viết 2 label để có thể hoạt động như vòng lặp whole và tính toán yêu cầu của bài. Nhưng phải lưu ý ban đầu sẽ có trường hợp giá trị của rdi sẽ là 0 và nếu ta truy cập vào địa chỉ đó thì sẽ bị lỗi. Nên phải xử lí trước trường hợp này.

```python
import pwn

pwn.context.update(arch="amd64")
output = pwn.process("/challenge/run")

asm = """
    cmp rdi, 0
    je .endloop
    xor rax, rax

    jmp .loop

    .loop:
        cmp byte ptr [rdi + rax], 0x00
        je .endloop

        add rax, 0x1

        jmp .loop

    .endloop:
        nop

"""

output.write(pwn.asm(asm))
print(output.readallS())
```

---

#### Flag
```pwn.college{swPCOpn83vVmA_T-MkWFTwMqV25.dRTMywCMxADNwEzW}```

---

### Level 29 - string-lower

---

### Tóm tắt đề bài

Chúng tôi sẽ kiểm tra code của bạn nhiều lần trong level này với các giá trị động!  
Điều này có nghĩa là code của bạn sẽ được chạy trong nhiều tình huống ngẫu nhiên để xác minh rằng logic đủ mạnh để hoạt động đúng trong quá trình sử dụng bình thường.  

Trong level này, bạn sẽ làm việc với `hàm (function)`!  
Điều này sẽ bao gồm việc thao tác với **instruction pointer (rip)**, cũng như thực hiện các tác vụ khó hơn bình thường.  
Bạn có thể sẽ cần dùng stack để lưu trữ giá trị hoặc gọi các hàm mà chúng tôi cung cấp cho bạn.  

Ở các level trước, bạn đã triển khai một vòng lặp `while` để đếm số byte liên tiếp khác 0 trong một vùng nhớ liên tục.  

Trong level này, bạn sẽ lại được cung cấp một vùng nhớ liên tục và sẽ lặp qua từng byte, thực hiện một phép toán có điều kiện cho đến khi gặp byte bằng 0.  
Tất cả sẽ nằm trong `một hàm`!  

Một **hàm** là một đoạn mã có thể gọi được mà không phá vỡ luồng điều khiển.  

Các hàm sử dụng lệnh **`call`** và **`ret`**.  

- **`call`** đẩy địa chỉ của lệnh kế tiếp lên stack, sau đó nhảy tới giá trị được lưu trong toán hạng.  
- **`ret`** thì ngược lại: nó lấy giá trị trên đỉnh stack và nhảy tới địa chỉ đó.  

Ví dụ với `call`:

    0x1021 mov rax, 0x400000
    0x1028 call rax
    0x102a mov [rsi], rax

- call đẩy 0x102a (địa chỉ của lệnh kế tiếp) lên stack.
- call nhảy tới 0x400000 (giá trị trong rax).

Ví dụ với `ret`:

                            Stack ADDR  VALUE
    0x103f mov rax, rdx         RSP + 0x8   0xdeadbeef
    0x1042 ret                  RSP + 0x0   0x0000102a
    
- Ở đây, ret sẽ nhảy tới 0x102a

Nhiệm vụ của bài:

    str_lower(src_addr):
    i = 0
    if src_addr != 0:
        while [src_addr] != 0x00:
        if [src_addr] <= 0x5a:
            [src_addr] = foo([src_addr])
            i += 1
        src_addr += 1
    return i


- foo được cung cấp tại địa chỉ 0x403000.
- foo nhận một byte làm tham số và trả về một byte.

Quy ước gọi hàm:

Tất cả các hàm (foo và str_lower) phải tuân thủ Linux amd64 calling convention (hay System V AMD64 ABI):

- Hàm str_lower nhận src_addr trong rdi.
- Hàm phải trả kết quả trong rax.

Lưu ý:

- src_addr là một địa chỉ trong bộ nhớ (nơi string được lưu).

- [src_addr] là byte tại địa chỉ đó.

Vì vậy:

- foo nhận một byte (giá trị) làm tham số đầu tiên.
- foo trả về một byte

---

#### Lời giải

Tương tự như những bài trên, bài này mình sẽ tạo ra những label tương ứng để sử dụng hoạt động như vòng lặp.

```python
import pwn

pwn.context.update(arch="amd64")
output = pwn.process("/challenge/run")

asm = """
    xor rax, rax
    cmp rdi, 0
    je .return

    .loop:
        cmp byte ptr [rdi], 0x00
        je .endloop

        cmp byte ptr [rdi], 0x5a
        jg .case2

        jmp .case1


    .case1:
        mov rbx, [rdi]
        push rdi                 
        push rax                 
        mov rdi, 0
        mov dil, bl              
        mov r10, 0x403000
        call r10                 
        mov bl, al               
        pop rax                  
        pop rdi                  
        mov [rdi], bl            
        add rax, 1
        add rdi, 0x1  
        jmp .loop

    .case2:
        add rdi, 0x1
        jmp .loop


    .endloop:
        jmp .return

    .return:
        ret
"""

output.write(pwn.asm(asm))
print(output.readallS())
```

---

#### Flag
```pwn.college{YdmHF_YqEjOkq2hyS51T56fgyhA.dVTMywCMxADNwEzW}```

---

### Level 30 - most-common-byte

---

#### Tóm tắt đề bài

Chúng tôi sẽ kiểm tra code của bạn nhiều lần trong level này với **giá trị động**!  

Điều này có nghĩa là chúng tôi sẽ chạy code của bạn theo nhiều cách ngẫu nhiên khác nhau để xác minh rằng logic đủ mạnh mẽ để hoạt động ổn định trong quá trình sử dụng bình thường.  

Trong level này, bạn sẽ làm việc với **hàm (functions)**!  
Điều này sẽ liên quan đến việc thao tác với **instruction pointer (`rip`)**, cũng như thực hiện các tác vụ khó hơn bình thường. Bạn có thể sẽ được yêu cầu sử dụng stack để lưu trữ giá trị hoặc gọi các hàm mà chúng tôi cung cấp cho bạn.  

Ở level trước, bạn đã học cách tạo hàm đầu tiên và cách gọi các hàm khác.  
Bây giờ, chúng ta sẽ làm việc với các hàm có **function stack frame**.  

Một **function stack frame** là một tập hợp các con trỏ và giá trị được push vào stack để lưu lại cho việc sử dụng sau này và cấp phát không gian trên stack cho các biến của hàm.  

Thanh ghi `rbp`
- `rbp` còn gọi là **Stack Base Pointer**.  
- Dùng để xác định nơi mà stack frame của chúng ta bắt đầu.  

Ví dụ, nếu ta muốn tạo một danh sách có 5 phần tử (mỗi phần tử là `dword`) chỉ dùng trong hàm:  

    ; thiết lập base của stack bằng top hiện tại
    mov rbp, rsp
    ; dịch stack xuống 0x14 byte (5 * 4)
    ; hành động như cấp phát bộ nhớ
    sub rsp, 0x14
    ; gán list[2] = 1337
    mov eax, 1337
    mov [rbp-0xc], eax
    ; thực hiện thêm các thao tác khác trên list ...
    ; khôi phục lại không gian đã cấp phát
    mov rsp, rbp

- rbp luôn được dùng để khôi phục stack về trạng thái ban đầu.
- Nếu không khôi phục stack → cuối cùng sẽ bị đầy.
- Chúng ta trừ từ rsp vì stack phát triển hướng xuống.
- Khi gán list[2], ta trừ đi 12 byte (3 dwords) vì stack tăng ngược.

Nhiệm vụ của bài:

    most_common_byte(src_addr, size):
    i = 0
    while i <= size-1:
        curr_byte = [src_addr + i]
        [stack_base - curr_byte * 2] += 1
        i += 1

    b = 0
    max_freq = 0
    max_freq_byte = 0
    while b <= 0xff:
        if [stack_base - b * 2] > max_freq:
        max_freq = [stack_base - b * 2]
        max_freq_byte = b
        b += 1

    return max_freq_byte

Giả định (Assumptions)

- Sẽ không bao giờ có nhiều hơn 0xffff của bất kỳ byte nào

- Kích thước (size) sẽ không bao giờ dài hơn 0xffff

- Danh sách luôn có ít nhất một phần tử

Ràng buộc (Constraints)

- Bạn phải đặt "counting list" trên stack

- Bạn phải khôi phục stack như một hàm bình thường

- Bạn không được phép thay đổi dữ liệu tại src_addr

---

### Lời giải

Tương tự như những bài trên, bài này mình sẽ tạo ra những label tương ứng để sử dụng hoạt động như vòng lặp.

```python
import pwn

pwn.context.update(arch="amd64")
output = pwn.process("/challenge/run")

asm = """
    

    .return:
        ret
"""

output.write(pwn.asm(asm))
print(output.readallS())
```

---

#### Flag
```pwn.college{YdmHF_YqEjOkq2hyS51T56fgyhA.dVTMywCMxADNwEzW}```

---