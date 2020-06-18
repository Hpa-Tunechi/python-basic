# Exception Handling
# Errors
# Three types of errors
# 1) Compile time error
# compile time error ah chuan spelling te, semicolon dah hmaih te leh engemaw dah hmaih te khan a ni.
# 2) Logical error
# Logical error ah kha chuan run lai khan a hriat loh a run zawh a a output ah khan a hriat chauh a ni.
# Output dik lo te a thlen a ni.
# 3) Run time error
# Run time error ah hi chuan a user/ a run tu khan input dik lo a chhut luh khan a rawn lang dawn a ni.
# entirnan integer data type te kha enter tur ni se string te lo enter daih ta ila. a dik dawn lo a ni.

# Error kan lo hmachhawn dan tur chu.

a = 5
b = 2
try:
    print(a/b)
except Exception as e:  # helaia e hian error awm kha a rawn print thei dawn a ni.
    print('Error a awm tlat mai', e)  # error a awm chauhin hei chu a print ang.
finally:  # finally hi chuan error a awm pawn awm loh pawn a rawn print dawn hrim hrim a ni.
    print('success')


# entirna sei deuhin aw. a error a zir ang khan chi hrang hrang a tih theih a ni.
try:
    i = int(input("Enter no. "))
    j = int(input('No. '))
    print(i)
    print(i/j)
except ValueError as v:  # tah hian value kan enter dik lo check na
    print('I enter value hi',v)
except ZeroDivisionError as z:  # zero divide a ni tih check na.
    print('I divide na hi. ', z)
except Exception as e:  # error hrim hrim check na.
    print('hei hi error aw.', e)
finally:
    print('Engkim check atanga hriat theih te an ni e.')
