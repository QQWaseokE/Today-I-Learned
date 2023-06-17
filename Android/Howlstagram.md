# 2023.05.23

#### activity_login.xml
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".LoginActivity">

    <ImageView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_above="@+id/signin_layout"
        android:layout_alignParentTop="true"
        android:src="@drawable/logo_title" />

    <LinearLayout
        android:id="@+id/signin_layout"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_alignParentBottom="true"
        android:orientation="vertical">

        <com.google.android.material.textfield.TextInputLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_marginLeft="20dp"
            android:layout_marginRight="20dp">

            <EditText
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:hint="@string/email" />
        </com.google.android.material.textfield.TextInputLayout>

        <com.google.android.material.textfield.TextInputLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_marginLeft="20dp"
            android:layout_marginRight="20dp">

            <EditText
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:hint="@string/password" />
        </com.google.android.material.textfield.TextInputLayout>


        <androidx.appcompat.widget.AppCompatButton
            android:layout_width="match_parent"
            android:layout_height="40dp"
            android:layout_marginLeft="20dp"
            android:layout_marginTop="15dp"
            android:layout_marginRight="20dp"
            android:layout_marginBottom="35dp"
            android:text="@string/signin_email"
            android:theme="@style/Buttonstyle" />

        <androidx.appcompat.widget.AppCompatButton
            android:layout_width="match_parent"
            android:layout_height="40dp"
            android:layout_marginLeft="20dp"
            android:layout_marginRight="20dp"
            android:layout_marginBottom="5dp"
            android:background="@drawable/btn_signin_facebook"
            android:text="@string/signin_facebook"
            android:textColor="@color/colorWhite" />

        <androidx.appcompat.widget.AppCompatButton
            android:layout_width="match_parent"
            android:layout_height="40dp"
            android:layout_marginLeft="20dp"
            android:layout_marginRight="20dp"
            android:layout_marginBottom="80dp"
            android:background="@drawable/btn_signin_google"
            android:text="@string/signin_facebook"
            android:textColor="@color/colorWhite" />
    </LinearLayout>

</RelativeLayout>

### 오류 발생
<img width="1689" alt="Screen Shot 2023-05-23 at 4 39 13" src="https://github.com/QQWaseokE/Today-I-Learned/assets/127533265/5b3e9f2f-07d7-41c0-a378-dc0aee9db1fc">

# 2023.05.31

activity_login.xml에서 테마를 변경해주고
color.xml에서 색상코드를 추가해주고
build.gradle에서 버전을 맞춰주는 등

Howlstagram_1.md에서 발생했던 오류를 모두 해결하고 로그인 화면을 성공적으로 띄웠다.

### 실습
<img width="1728" alt="Screenshot 2023-05-31 at 0 46 53" src="https://github.com/QQWaseokE/Today-I-Learned/assets/127533265/d51adc95-e3b9-4246-8987-ca541ff941e3">

# 2023.06.05

강의와 현 시점의 안드 스튜디오의 버전이 맞지 않아 오류가 발생하였다.
오류 수정중...

### 실습
<img width="1728" alt="Screenshot 2023-06-05 at 23 23 22" src="https://github.com/QQWaseokE/Today-I-Learned/assets/127533265/d0f6c8a1-b78c-44d2-b25d-e8246495ffe0">

