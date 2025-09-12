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

### Bảng chân trị tham khảo:

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