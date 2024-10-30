import numpy as np
from spatialmath import *
from math import pi

import matplotlib.pyplot as plt

%matplotlib widget


T1 = SE3.Tx(1)

plt.figure() # create a new figure
SE3().plot(frame='0', dims=[-3,3], color='black')
T1.plot(frame='1')

T2= T1*T1

plt.figure()
SE3().plot(frame='0',dims=[-3,3],color='black')
T1.plot(frame='1',color='red')
T2.plot(frame='2')

T2= T1**2
T2=T1
T2*=T1

T2

SE3.Tz(4)

SE3.Ty(3)

SE3(7,8,9)

SE3.Tx(7)*SE3.Ty(8)*SE3.Tz(9)

SE3.Ty(2).inv()

SE3.Ty(2)*SE3.Ty(2).inv()

P= [1,2,3]

SE3(4,5,6) * P 

R1 = SO3.Rx(pi/4)

fig = plt.figure()
SE3().plot(frame='0',color='black',dims=[0,2])
R1.plot(frame='1')

R2 = R1* R1

fig = plt.figure()
SE3().plot(frame='0',color='black',dims=[0,2])
R1.plot(frame='1',color='red')
R2.plot(frame='2')

R2 = R1**2

R1 = SO3.Rx(45,'deg')

R3 = SO3.RPY([10,20,30],unit ='deg')

plt.figure() 
SE3().plot(frame='0',color='black',dims=[0,2])
R3.plot(frame='3')

R3.rpy(unit='deg')

R1

SO3.Rz(pi/4)

SO3.Rz(pi/4).inv()

SO3.Rz(pi/4)* SO3.Rz(pi/4).inv()

SO3()

SO3.OA(o=[0,0,-1],a=[1,0,0])

SO3.AngVec(pi/4,[1,0,0])


SO3.AngVec(30,[1,2,3],unit='deg')

T1 = SE3(1,2,3)* SE3.Rx(30,'deg')

plt.figure()

SE3().plot(frame='0',dims=[0,3],color='black')
T1.plot(frame='1')

T2 = SE3.Rx(30,'deg')*SE3(1,2,3)

T2.plot(frame='2',color='red')

P=[1,2,1]
T1*P

T1.inv()*P

T1.n

T1.R

T1.t

P = np.array([[-1, 1, 1, -1, -1, 1, 1, -1], [-1, -1, 1, 1, -1, -1, 1, 1], [-1, -1, -1, -1, 1, 1, 1, 1]])
P

Q= T1* P 

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.scatter(xs=Q[0],ys=Q[1],zs=Q[2],s=20)


lines = [[0,1,5,6],[1,2,6,7],[2,3,7,4],[3,0,4,5]]
ax.set_xlim3d(-2, 3); ax.set_ylim3d(0, 5); ax.set_zlim3d(0, 5);
ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z');
for line in lines:
    ax.plot([Q[0,i] for i in line], [Q[1,i] for i in line], [Q[2,i] for i in line])


T = [SE3.Rx(0),SE3.Rx(0.1),SE3.Rx(0.2),SE3.Rx(0.3),SE3.Rx(0.4)]

T = SE3( [ SE3.Rx(0), SE3.Rx(0.1), SE3.Rx(0.2), SE3.Rx(0.3), SE3.Rx(0.4)] )

type(T)

len(T)

T

T[3]

T[1:-1:2]

T.append(SE3.Rx(0.5))
len(T)

T = SE3.Rx (np.linspace(0,0.5,5))
len(T)

T2 = SE3.Ry(40,'deg')

A = T*T2
len(A)

B = T2 * T 
len(B)

C = T*T
len(C)

P = T * [0,1,0]
P 

for x in T:
    Q = x * P 

np.array([x*[0,1,0]for x in T])   


q1 = Quaternion([1,2,3,4])
q1

q2 = Quaternion([5,6,7,8])
q2

q1 + q2

q1- q2

q1*q2

q1.s

q1.v

q1.vec
q1.conj()

q1.norm()

q1* q1.conj()

Quaternion.Pure([1,2,3])

q1 = UnitQuaternion.Rx(30,'deg')
q1

q1.norm()

q2= UnitQuaternion.Ry(-40,'deg')
q2

q3 = q1*q2
q3

q3.R

SO3.Rx(30,'deg') * SO3.Ry (-40,'deg')

q2.inv()

q1*q2.inv()

q1/q2

q1.SO3()

q1.vec3

a = UnitQuaternion.qvmul(q1.vec3,q2.vec3)
a

UnitQuaternion.Vec3(a)

R= SO2 (pi/4)
R

SO2 (45,unit='deg')

plt.figure()
R.plot()

T = SE2 (1,2)
T

T = SE2 ([1,2])

plt.figure()
T.plot()
plt.grid(True)

T = SE2 (1,2) * SE2(45,unit ='deg')
T

plt.figure()
T.plot()
plt.grid(True)