def main():
    def second_calculater():
        year = int(input("Enter a year: "))

        time_units = {
            "days" : 365,
            "hours" : 24,
            "minutes" : 60,
            "seconds" : 60,
        }

        leap_year = False
        if year % 4 == 0:
            time_units["days"] = 366
            leap_year = True

        seconds_in_year = 1
        for unit,value in time_units.items():
            seconds_in_year *= value

            
        if leap_year:
            print(f"There are  {seconds_in_year} seconds in a year because this is leap year!")
        else:
            print(f"There are  {seconds_in_year} seconds in a year!") 
    second_calculater()

if __name__ == '__main__':
    main()

AIzaSyBQsAGRXuBkakRaYT-fCgXmJEgSLdFd0B0