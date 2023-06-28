#/usr/bin/python

# Booking room
# Scope booking only in a month, day 1 to 31 and must book at least one night
mode = input('Enter mode (q - quit, b = booking, c = cancel, p = print booking): ')

# Array of dictionary
bookings = []

while mode != 'q':
    if mode == 'b':

        # Validate input
        is_valid_input = False
        while not is_valid_input:
            checkin_day = int(input('Enter checkin day: '))
            checkout_day = int(input('Enter chechout day: '))

            if checkin_day < 1 or checkin_day > 30 and checkout_day < 2 and checkout_day > 31:
                print('Invalid checin day or checkout day, please re-enter')
            elif checkin_day >= checkout_day:
                print('Checkin day must be less than checkout day, please re-enter')
            else:
                is_valid_input = True

        is_available = True

        for booking in bookings:
            # booking is dictionary containing booking no, checkin_day and checkout_day
            # If user will book the room but the room is already booked, then the room is not available.
            # There are 3 cases that user cannot book the room:
            # 1. Checkin day is between **booking** checkin day and checkout day
            # 2. Checkout day is between **booking** checkin day and checkout day
            # 3. **Booking** checkin day is between checkin day and checkout day (but checkout day is not between booking checkin day and checkout day)
            #
            # Logic: If there is a booking between checkin day and checkout day, then the room is not available
            #                   |<--->|
            #                               |<--->|
            #       |<--->|
            #
            #          i----o Case 1
            #     i----o      Case 2
            #     i---------o Case 3
            #                      i----o Case 1
            #                 i----o      Case 2
            #                 i---------o Case 3
            #
            #  i----o Can booking
            #             i---o  Can booking
            #
            # i = checkin day
            # o = checkout day
            #
            # See i and o on above diagram.
            # User cannot book if o greater than booking checkedin day **and** i less than booking checkout day

            if checkin_day < booking['checkout_day'] and checkout_day > booking['checkin_day']:
                is_available = False

                print("Room not available, there is a booking between {0}-{1}".format(booking['checkin_day'], booking['checkout_day']))
                break

        if is_available:
            booking_no = 'b' + "{:02d}".format(checkin_day) + "{:02d}".format(checkout_day)
            bookings.append({ 'booking_no': booking_no, 'checkin_day': checkin_day, 'checkout_day': checkout_day })
            print('Booking success')

    elif mode == 'c':
        booking_no = input('Enter booking no: ')

        for booking in bookings:
            if booking['booking_no'] == booking_no:
                bookings.remove(booking)
                print('Cancel success')
                break
        else:
            print('Cancel failed (booking no not found)')

    elif mode == 'p':
        for booking in bookings:
            print(booking)

    mode = input('Enter mode (q - quit, b = booking, c = cancel, p = print booking): ')
