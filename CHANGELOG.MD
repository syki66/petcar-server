2020-09-27

- 서보모터 파이썬코드 함수화해서 하나로 합치고, 서버에 기능 추가함
- rgb led pwm 제어가 반드시 기간을 가지고 있어야 해서 서버로 제어하는 방법밖에 없는데 실패했고, 그냥 rgb led를 7가지 색의 디지털 제어로만 서버에 추가함
- rgb led와 servo의 gpio cleanup을 각각의 핀만 하도록 수정함

---

2020-09-26

- 서보모터 on/off 제어하는 파이썬 코드 추가

---

2020-09-18

- dc motor 제어하는 파이썬 파일을 함수에서 클래스로 변경
- dc_motor 제어 클래스를 연속제어 기준으로 수정한 뒤, 순간제어도 가능하도록 새 클래스에 상속 및 오버라이딩 했음 (python3 버전 사용해야 오버라이딩 에러안남)

---