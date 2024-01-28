# decode_string
바이너리에 존재하는 난독화 된 문자열들은 일반적으로 런타임에 난독화가 해제된다. 이 때, 난독화 해제를 위해 공통적으로 호출하는 함수(한 개 뿐이라는 보장은 없다)가 존재하는데, 해당 함수를 호출하는 곳을 찾아 IDB(IDA Database) 파일 상에서 난독화를 해제시켜 패치한다. `src/decode_string.py`는 이를 자동화하기 위한 IDAPython 스크립트이다. 

이 예제는 기초적인 템플릿을 제공할 뿐, 바이너리마다 난독화 해제 루틴은 상이하므로 직접 분석하여 최적화 된 스크립트를 재작성해야한다. 참고로 이 스크립트는 난독화 해제 시 함수를 호출한다는 것을 전제로 하기 때문에 `inline` 키워드로 컴파일 된 함수는 탐지가 어렵다.

## Results
- Before

![image](https://user-images.githubusercontent.com/49597086/128155181-2abfc218-185c-46b4-9bbd-d59f842b5a81.png)
![image](https://user-images.githubusercontent.com/49597086/128155332-2dafcd5d-54e9-45d8-95a9-282a8acb1021.png)
![image](https://user-images.githubusercontent.com/49597086/128155431-fe14956b-efe3-4e14-8979-0b9f964145f6.png)

- After

![image](https://user-images.githubusercontent.com/49597086/128155798-b29b2104-d889-4560-852e-cb3c9a22d4d2.png)
![image](https://user-images.githubusercontent.com/49597086/128155847-12b6326a-a038-485b-a6cd-dd1a5c4e521b.png)
![image](https://user-images.githubusercontent.com/49597086/128155887-06375e39-a214-4bb9-878a-9c437f0f9445.png)
