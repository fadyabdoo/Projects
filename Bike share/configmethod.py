def display_raw_input(city)
    display_raw = input("Enter 'yes' for look about raw data or 'no' \n").lower()
    while display_raw=='yes':
        try:
            for chunk in pd.read_csv(CITY_DATA[city],chunksize=5):
                print(chunk)
                display_raw = input("Enter 'yes' for look about raw data or 'no' \n").lower()
                if display_raw != 'yes':
                    print("Thankyou")
                    break
            break
        except:
            print("thankYou")
                
                
           
        