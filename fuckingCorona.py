import random


class Nation:

    def __init__(self, name, number, population, infectee):
        self.name = name
        self.number = number
        self.population = population
        self.infectee = infectee

    # 백신의 치료율에 따라 감염자 수를 감소시키는 함수
    # 치료자가 생길때마다 그 값을 치료자 리스트에 원소로 추가
    def cure(self):
        if self.infectee > 0:
            if vaccine_num == vac1.vacNumber:
                curedPopulation.append(self.infectee * 0.25)
                self.infectee = self.infectee * 0.75
            if vaccine_num == vac2.vacNumber:
                curedPopulation.append(self.infectee * 0.5)
                self.infectee = self.infectee * 0.5
            if vaccine_num == vac3.vacNumber:
                curedPopulation.append(self.infectee)
                self.infectee = self.infectee * 0

    # 완치되지 않은 국가만 출력
    def printResult(self):
        if self.infectee > 0:
            print('감염 국가:', self.name)
            print('인구수:', self.population, '명')
            print('감염 인구수: ', int(self.infectee), '명\n')

    # 최종결과 프린트를 위한 코드
    def finalPrintResult(self, rank):
        print('순위: {}위'.format(rank))
        print('감염 국가: ', self.name)
        print('인구수: ', self.population, '명')
        print('감염 인구수: ', int(self.infectee), '명\n')


class Vaccine:

    def __init__(self, vacName, vacNumber, percent):
        self.vacName = vacName
        self.vacNumber = vacNumber
        self.percent = percent

    # 백신 정보 출력
    def printVaccine(self):
        print('백신 이름: {0}'.format(self.vacName))
        print('백신 치료율: {} % \n'.format(self.percent))


class MainFunc:

    # 감염자수가 없는 국가만 정보 출력
    def allPrintResult(self):
        korea.printResult()
        china.printResult()
        japan.printResult()
        usa.printResult()
        germany.printResult()

    # 감염자가 많은 국가 순으로 정렬 (내림차순)
    def infecteesOfNationsSortedByDesc(self):

        nations = [korea, china, japan, usa, germany]
        sorted_nations = []  # 감염자 수가 많은 나라부터 담을 배열 생성
        rank = 1

        while nations:
            large = nations[0]  # 첫 번째 국가를 large 변수에 저장 -> 비교대상
            for i in range(0, len(nations) - 1):
                if nations[i].infectee > nations[i + 1].infectee:
                    large = nations[i]
                    nations[i] = nations[i + 1]
                    nations[i + 1] = large
                else:
                    large = nations[i + 1]
            sorted_nations.append(large)
            nations.remove(large)

        for nation in sorted_nations:
            nation.finalPrintResult(rank)
            rank = rank + 1

    # 감염자 수에 관계없이 모든 국가정보 출력
    def cureProcess(self):
        if nation_num == korea.number and korea.name not in curedNation:
            korea.cure()
        elif nation_num == china.number and china.name not in curedNation:
            china.cure()
        elif nation_num == japan.number and japan.name not in curedNation:
            japan.cure()
        elif nation_num == usa.number and usa.name not in curedNation:
            usa.cure()
        elif nation_num == germany.number and germany.name not in curedNation:
            germany.cure()

    # 완치된 국가를 리스트에서 감염국 리스트에서 제외하는 함수
    def curedNationRemove(self):
        if vaccine_num == vac3.vacNumber:
            if korea.number in infectedNationName and nation_num == korea.number:
                infectedNationName.remove(korea.number)
            if china.number in infectedNationName and nation_num == china.number:
                infectedNationName.remove(china.number)
            if japan.number in infectedNationName and nation_num == japan.number:
                infectedNationName.remove(japan.number)
            if usa.number in infectedNationName and nation_num == usa.number:
                infectedNationName.remove(usa.number)
            if germany.number in infectedNationName and nation_num == germany.number:
                infectedNationName.remove(germany.number)

    # 완치된 국가의 리스트에 국가명을 담는 함수
    def curedNationadd(self):
        if vaccine_num == vac3.vacNumber:
            if nation_num == korea.number and korea.name not in curedNation:
                curedNation.append(korea.name)
            if nation_num == china.number and china.name not in curedNation:
                curedNation.append(china.name)
            if nation_num == japan.number and japan.name not in curedNation:
                curedNation.append(japan.name)
            if nation_num == usa.number and usa.name not in curedNation:
                curedNation.append(usa.name)
            if nation_num == germany.number and germany.name not in curedNation:
                curedNation.append(germany.name)

    # 국가와 백신을 선택하고 정보를 출력하는 함수
    def selectResult(self):
        print('★', game_round, "번째시도★\n")
        if vaccine_num == vac1.vacNumber:
            print('선택된 백신:', vac1.vacName, ',', '치료율:', vac1.percent, '%')
        elif vaccine_num == vac2.vacNumber:
            print('선택된 백신:', vac2.vacName, ',', '치료율:', vac2.percent, '%')
        else:
            print('선택된 백신:', vac3.vacName, ',', '치료율:', vac3.percent, '%')
        if nation_num == korea.number:
            print('선택된 나라:', korea.name, ',', '인구수:', korea.population, '명', ',', '감염자수:', int(korea.infectee), '명')
        elif nation_num == china.number:
            print('선택된 나라:', china.name, ',', '인구수:', china.population, '명', ',', '감염자수:', int(china.infectee), '명')
        elif nation_num == japan.number:
            print('선택된 나라:', japan.name, ',', '인구수:', japan.population, '명', ',', '감염자수:', int(japan.infectee), '명')
        elif nation_num == usa.number:
            print('선택된 나라:', usa.name, ',', '인구수:', usa.population, '명', ',', '감염자수:', int(usa.infectee), '명')
        else:
            print('선택된 나라:', germany.name, ',', '인구수:', germany.population, '명', ',', '감염자수:', int(germany.infectee),
                  '명')

    # 5라운드일 경우를 제외하고 감염자수가 0이 아닌 국가에 인구수 대비 15%의 감염자를 추가
    # 그 후 감염자수를 나타내는 리스트에 값을 원소로 추가
    def infecteeIncrease(self):
        if game_round != 5:
            if korea.infectee > 0:
                korea.infectee = korea.infectee + 225
                infectedPopulation.append(225)
            if china.infectee > 0:
                china.infectee = china.infectee + 450
                infectedPopulation.append(450)
            if japan.infectee > 0:
                japan.infectee = japan.infectee + 300
                infectedPopulation.append(300)
            if usa.infectee > 0:
                usa.infectee = usa.infectee + 375
                infectedPopulation.append(375)
            if germany.infectee > 0:
                germany.infectee = germany.infectee + 330
                infectedPopulation.append(330)

    # 백신3을 썼을때만 완치가 되므로 백신 3을 선택했을시 선택된 국가를 출력하고,
    # 모든 국가가 왼치될시 모든 국가가 완치됐다는 메세지 출력
    def processResult(self):
        print("==============================================")
        if vaccine_num == vac3.vacNumber:
            if nation_num == korea.number:
                print('완치된 국가:', korea.name, '\n')
            elif nation_num == china.number:
                print('완치된 국가:', china.name, '\n')
            elif nation_num == japan.number:
                print('완치된 국가:', japan.name, '\n')
            elif nation_num == usa.number:
                print('완치된 국가:', usa.name, '\n')
            elif nation_num == germany.number:
                print('완치된 국가:', germany.name, '\n')
            else:
                print("")

        print(game_round, '차 백신 투여 후 감염된 나라에 대한 정보')
        print("==============================================")
        if (korea.infectee == 0 and
                china.infectee == 0 and
                japan.infectee == 0 and
                usa.infectee == 0 and
                germany.infectee == 0):
            print('모든 국가가 완치되었습니다!!!')

        else:
            main.allPrintResult()

    # 최종결과창 출력
    def finalResult(self):
        print('====================================')
        print('              최종결과              ')
        print("====================================")
        print("라운드마다 추가로 감염된 감염자 수:", sum(infectedPopulation), '명')  # 감염자수 리스트 원소들의 총합
        print("백신으로 치료된 감염자 수: ", int(sum(curedPopulation)), '명')  # 치료자수 리스트 원소들의 총합
        print('백신으로 완치된 국가:', ' '.join(curedNation), '(', len(curedNation), '개 )\n')  # 치료된 국가의 개수와 리스트 출력

        main.infecteesOfNationsSortedByDesc()


korea = Nation('한국', 1, 1500, 300)
china = Nation('중국', 2, 3000, 800)
japan = Nation('일본', 3, 2000, 500)
usa = Nation('미국', 4, 2500, 750)
germany = Nation('독일', 5, 2200, 1000)

infectedNationName = [korea.number, china.number, japan.number, usa.number, germany.number]

# 완치된 국가, 치료자수 및 누적 감염자수를 기록하여 출력하기 위한 빈 리스트 선언
curedNation = []
curedPopulation = []
infectedPopulation = []

vac1 = Vaccine('백신1', 1, 25)
vac2 = Vaccine('백신2', 2, 50)
vac3 = Vaccine('백신3', 3, 100)

VaccineList = [vac1.vacNumber, vac2.vacNumber, vac3.vacNumber]

main = MainFunc()

# 4번을 누르기 전까지 메뉴를 출력
while True:

    print('-----------------------')
    print('    코로나 종식 게임    ')
    print('-----------------------')
    print('1. 백신 정보')
    print('2. 감염된 국가 정보')
    print("3. 게임 시작")
    print("4. 게임 종료\n")
    num = int(input('원하시는 항목을 선택하세요 : '))
    print("")

    # 백신 정보 출력
    if num == 1:
        vac1.printVaccine()
        vac2.printVaccine()
        vac3.printVaccine()

        # 국가 정보 출력
    elif num == 2:
        main.allPrintResult()

        # 메인게임
    elif num == 3:
        game_round = 1
        vaccine_num, nation_num = map(int, input('사용할 백신(1-3)과 백신을 적용할 국가(1-5)의 번호를 차례대로 입력하세요.').split())
        while vaccine_num > 3 or nation_num > 5:  # 예외처리
            print("입력 범위를 벗어났습니다. 다시 선택해주세요.")
            vaccine_num, nation_num = map(int, input('사용할 백신(1-3)과 백신을 적용할 국가(1-5)의 번호를 차례대로 입력하세요.').split())
            if vaccine_num < 3 and nation_num < 5:
                break
        print("")
        main.selectResult()
        main.cureProcess()
        main.curedNationRemove()
        main.curedNationadd()
        main.processResult()
        main.infecteeIncrease()

        game_round = game_round + 1

        while game_round < 6:
            # random.shuffle(VaccineList)
            # vaccine_num = random.randint(1, len(VaccineList))
            # random.shuffle(infectedNationName)
            # nation_num = random.randint(1, len(infectedNationName))
            # while nation_num not in infectedNationName:
            #     nation_num = random.randint(1, len(infectedNationName))

            random.shuffle(VaccineList)
            vaccine_num = random.choice(VaccineList)
            random.shuffle(infectedNationName)
            nation_num = random.choice(infectedNationName)

            if (korea.infectee > korea.population or
                    china.infectee > china.population or
                    japan.infectee > japan.population or
                    usa.infectee > usa.population or
                    germany.infectee > germany.population):
                print("감염자 수가 인구 수보다 많은 국가가 발생하였습니다. 게임을 중단합니다!")
                break

            main.selectResult()
            main.cureProcess()
            main.curedNationRemove()
            main.curedNationadd()
            main.processResult()
            main.infecteeIncrease()
            game_round = game_round + 1

        main.finalResult()
        print(curedNation)

        # 게임종료
    elif num == 4:
        print('게임을 종료합니다.')
        break
    # 예외처리
    else:
        print('다시 번호를 입력하세요')