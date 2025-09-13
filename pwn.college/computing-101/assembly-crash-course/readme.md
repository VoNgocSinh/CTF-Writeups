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