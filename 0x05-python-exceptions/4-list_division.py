#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            # Try to perform the division
            result.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            # Handle division by zero
            print("division by 0")
            result.append(0)
        except (ValueError, TypeError):
            # Handle wrong type
            print("wrong type")
            result.append(0)
        except IndexError:
            # Handle out of range
            print("out of range")
            result.append(0)
        finally:
            # Ensure any exceptions are caught & cont. with next iteration
            pass

    return result
