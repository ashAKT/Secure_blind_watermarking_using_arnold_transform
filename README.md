# Secure_watermarking_using_Arnold_Transform

Arnold Transformation performs matrix(N x N) transformation on the image. Major benefit of Arnold transformation is that the number of times Arnold transformation applied while encrypting the image, then while decrypting the same number of Arnold transform would decrypt the watermark image as shown below.

![arnold-1](https://user-images.githubusercontent.com/25420334/124324974-7ee3ad80-dba1-11eb-925b-71bf2b79357e.jpg)

The Arnold Transform formula for two dimensional signal NxN can be defined as follows:

![arnold_encypt1](https://user-images.githubusercontent.com/25420334/124325380-1a751e00-dba2-11eb-8a36-a769bb328c41.jpg)

Where y Є (0,1,2…. N-1), (x1,y1) indicates the coordinate pixel points in the original matrix, (x2,y2) indicates the coordinates of the pixel after transformation. Inverse Arnold Transform is used to decrypt the Arnold encrypted message using the following equation:

![arnold_dencypt1](https://user-images.githubusercontent.com/25420334/124325447-3ed0fa80-dba2-11eb-8100-b91e1cc08936.jpg)

Inverse of any matrix can be calculated as:

![Inverse of a matrix](https://user-images.githubusercontent.com/25420334/124325610-95d6cf80-dba2-11eb-9cd3-7fd9889f8387.png)

Source--> https://www.mathsisfun.com/algebra/matrix-inverse.html

## Note: 
You can also use variables(a,b,... etc) in the matrix to make it more complex as shown below

Arnold Transform:

![arnold_encypt2](https://user-images.githubusercontent.com/25420334/124325958-3cbb6b80-dba3-11eb-99c7-bae1570102b8.jpg)

Inverse Arnold Transform will be:

![arnold_decrypt2](https://user-images.githubusercontent.com/25420334/124326020-5d83c100-dba3-11eb-9ba9-6640b884a9ff.jpg)

## Operation: Flow Chart of Arnold Image Transform Technique

![asheet_arnold](https://user-images.githubusercontent.com/25420334/124326389-e4389e00-dba3-11eb-96aa-492309155846.png)

## Softwares & Packages Required:

1. Python
```javascript
sudo apt install python3
```
2. pip: pip is a python package manager helps to install python packages. Documentation --> https://pypi.org/project/pip/
```javascript
python3 -m pip install
```
4. Python packages:
- numpy: Documentation --> https://numpy.org/
```javascript
pip install numpy
```
- opencv-python: Documentation --> https://pypi.org/project/opencv-python/
```javascript
pip install opencv-python
```
- setuptools: Documentation --> https://pypi.org/project/setuptools/
```javascript
pip install setuptools
```
- blind-watermark: Documentation with screenshots --> https://pypi.org/project/blind-watermark/
```javascript
pip install blind-watermark
```
- PyWavelets: Documentation --> https://pypi.org/project/PyWavelets/
```javascript
pip install PyWavelets
```
- Pillow: Documentation --> https://pypi.org/project/Pillow/
```javascript
pip install Pillow
```

## PROGRAMMING

Methods Used:
1. Arnold Transformation on the watermark logo (Source code--> https://github.com/AleDiBen/ArnoldTransform)
```javascript
perform_arnold_transform (watermark_logo)
```
2. Blind Watermarking (Source code--> https://pypi.org/project/blind-watermark/)
```javascript
blind_watermark (img_orgnl, scrambled_img)
```
3. Extract the watermark logo
```javascript
extract_watermark (embed_img)
```
4. Inverse Arnold Transformation
```javascript
inverse_arnold_transform (scram_watermark)
```
## Screenshots:

![asheet_arnold1](https://user-images.githubusercontent.com/25420334/124364394-ddbb2c80-dc5e-11eb-9ba5-310d9e044eb9.jpg)

![asheet_arnold2](https://user-images.githubusercontent.com/25420334/124364401-ef9ccf80-dc5e-11eb-8384-b6b70c851391.jpg)

## Limitations of Arnold Transformation:
1.	Only restricted to 2D images.
2.	Cannot be extended to text or audio because arnold transform is an image encryption technique.
3.	Traditional scrambling technique based on Arnold Transformation only applies to square area. However, research is happening to extend Arnold scrambling to non-square images[5].
4.	Traditional scrambling technique based on Arnold Transformation only applies to binary image i.e image having only two colours. Arnold Transformation combined with various  image transform are used for colour image encryption[6].

## Performance Parameters realised to analyze the robustness of watermarked image [1-3]:
(Not implemented in this repository)
1. Normalized Correlation(NC)
2. Peak Signal to Noise Ration(PSNR)
3. Bit Error Rate(BER)
4. Structural Similarity Index Matrix(SSIM)

## Various Watermark Attacks:
Major threat in digital watermarking are attacks such as image processing attack, geometric attacks, cryptographic attacks, and protocol attack [4].

## References:
1.	Zhaofeng, Ma, Huang Weihua, and Gao Hongmin. "A new blockchain-based trusted DRM scheme for built-in content protection." EURASIP Journal on Image and Video Processing 2018.1 (2018): 1-12.
2.	Thanki, Rohit, and Ashish Kothari. ``Multi-level security of medical images based on encryption and watermarking for telemedicine applications." Multimedia Tools and Applications 80.3 (2021): 4307-4325.
3.	Kumar, Chandan, Amit Kumar Singh, and Pardeep Kumar. "Dual watermarking: An approach for securing digital documents." Multimedia Tools and Applications (2019): 1-16.
4.	Garg, Preeti, and R. Rama Kishore. "Performance comparison of various watermarking techniques." Multimedia Tools and Applications 79.35 (2020): 25921-25967.
5.	Min, Li, Liang Ting, and He Yu-jie. "Arnold transform based image scrambling method." 3rd International Conference on Multimedia Technology (ICMT-13). Atlantis Press, 2013.
6.	Vaish, Ankita, and Manoj Kumar. "Color image encryption using MSVD, DWT and Arnold transform in fractional Fourier domain." Optik 145 (2017): 273-283.
7.	Arnold Transform Source Code --> https://github.com/AleDiBen/ArnoldTransform
8.	Blind Watermarking Source Code --> https://pypi.org/project/blind-watermark/

## ---> Please let me know if this repository is helpful to you <---
