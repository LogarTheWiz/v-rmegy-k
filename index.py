import statistics;
counties = [];
with open('./vármegyék.csv', 'r' ,encoding='utf-8') as forras:
    next(forras);
    for sor in forras:
        adatok = sor.strip().split(',');
        county = {'name':adatok[0],'capital':adatok[1],'size':adatok[2],'cities':adatok[3], 'pop/size':adatok[4], 'pop':adatok[5], 'region':adatok[6]};
        counties.append((county));
def sortkey0(e):
    return e['name'];
def sortkey1(e):
    return e['capital'];
def sortkey2(e):
    return e['size'];
def sortkey3(e):
    return e['cities'];
def sortkey4(e):
    return e['pop/size'];
def sortkey5(e):
    return e['pop'];
def sortkey6(e):
    return e['region'];
class County:
    def __init__(self,name,capital,size,cities,popsize,pop,region):
        self.name = name;
        self.capital = capital;
        self.size = size;
        self.cities = cities;
        self.popsize = popsize;
        self.pop = pop;
        self.region = region;
    def searchforbiggestpop():
        tempcounties = counties;
        tempcounties.sort(reverse=True,key=sortkey5);
        return tempcounties[0];
    def searchforsmallestsize():
        tempcounties = counties;
        tempcounties.sort(key=sortkey2);
        return tempcounties[0];
    def avgpop():
        avg = 0;
        popsize = 0;
        counter = 0;
        for county in counties:
            popsize = popsize + int(county['pop/size']);
            counter += 1;
        avg = popsize / counter;
        print(avg);
    def capname():
        for county in counties:
            print(county['name']);
    def regions():
        regions = [];
        for county in counties:
            if regions.count(county['region']) < 1:
                regions.append(county['region']);
            else:
                pass;
        i = 0;
        stats = [];
        while i < len(regions):
            for county in counties:
                if county['region'] == regions[i]:
                    stats[i] += 1;
            i += 1;
        i = 0;
        while i < len(regions):
            print(f'{regions[i]}:{stats[i]}');
    def maxcity():
        tempcounties = counties;
        tempcounties.sort(key=sortkey3);
        return tempcounties[0];
    def toppop():
        tempcounties = counties;
        tempcounties.sort(key=sortkey5);
        i = 0;
        while i < 5:
            print(tempcounties[i]);
            i+=1;
    def sokember():
        tempcounties = [];
        for county in counties:
            if int(county['pop/size']) > 100:
                tempcounties.append(county)
        print(tempcounties);
    def search():
        imp = str(input('Adj meg egy megyét!\n '));
        for county in counties:
            if county['name'] == imp:
                print(county);
    def smallpop():
        tempcounties = counties;
        tempcounties.sort(key=sortkey5);
        return tempcounties[0];
    def searchforbiggestsize():
        tempcounties = counties;
        tempcounties.sort(key=sortkey2,reverse=True);
        return tempcounties[0];
    def avgcity():
        avg = 0;
        citycount = 0;
        counter = 0;
        for county in counties:
            citycount = citycount + int(county['cities']);
            counter += 1;
        avg = citycount / counter;
        print(avg);
    def regionpop():
        regions = [];
        for county in counties:
            if regions.count(county['region']) < 1:
                regions.append(county['region']);
            else:
                pass;
        i = 0;
        pop = [0];
        while i < len(regions):
            pop.append(0);
            i+=1;
        i = 0;
        while i < len(regions):
            for county in counties:
                if county['region'] == regions[i]:
                    pop[i] += int(county['pop']);
            i += 1;
        with open('./regio_osszlakossag.txt', 'w' ,encoding='utf-8') as result:
            i = 0;
            result.write('Régió,Népesség')
            while i < len(regions):
                result.write(f'{regions[i]},{pop[i]}\n');
                i+=1;
County.regionpop();