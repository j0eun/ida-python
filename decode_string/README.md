# decode_string
바이너리에서 난독화된 문자열을 사용하는 경우, 일반적으로 난독화를 해제하고 사용한다. IDB(IDA Database) 파일 상에서 정적으로 난독화를 해제시켜 패치한다. 이를 자동화하기 위한 idapython 스크립트. 바이너리마다 루틴을 분석한 뒤 최적화된 스크립트를 따로 작성해주어야 하며, 이 예제는 그를 위한 기초적인 토대를 제공한다.

# Results
- Before

![image](https://user-images.githubusercontent.com/49597086/128155181-2abfc218-185c-46b4-9bbd-d59f842b5a81.png)
![image](https://user-images.githubusercontent.com/49597086/128155332-2dafcd5d-54e9-45d8-95a9-282a8acb1021.png)
![image](https://user-images.githubusercontent.com/49597086/128155431-fe14956b-efe3-4e14-8979-0b9f964145f6.png)

- After

![image](https://user-images.githubusercontent.com/49597086/128155798-b29b2104-d889-4560-852e-cb3c9a22d4d2.png)
![image](https://user-images.githubusercontent.com/49597086/128155847-12b6326a-a038-485b-a6cd-dd1a5c4e521b.png)
![image](https://user-images.githubusercontent.com/49597086/128155887-06375e39-a214-4bb9-878a-9c437f0f9445.png)
