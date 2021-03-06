import numpy as np
import matplotlib.pyplot as plt

def disGeometryGprMax(x, y, z, resolution):
    """
    deiscret geometryfunction in different parts
    """
    i=0
    xn = np.array([0], dtype=float)
    yn = np.array([0], dtype=float)
    zn = np.array([0], dtype=float)

    for n in range(0, len(y)):
        if n == 0:
            xn[0] = round(x[0]/resolution)* resolution
            yn[0] = round(y[0]/resolution)* resolution
            zn[0] = round(z[0]/resolution)* resolution
        
        if (y[n]-yn[-1]) >=resolution:                 
            fitX = round((x[n]-xn[-1])/resolution)* resolution
            fitY = round((y[n]-yn[-1])/resolution)* resolution
            xn = np.append(xn, xn[-1]+fitX)
            yn = np.append(yn, yn[-1])
            zn = np.append(zn, zn[-1])
            xn = np.append(xn, xn[-1])
            yn = np.append(yn, yn[-1]+fitY)
            zn = np.append(zn, zn[-1])

        if (z[n]-zn[-1]) >=resolution:
            fitX = round((x[n]-xn[-1])/resolution)* resolution
            fitZ = round((z[n]-zn[-1])/resolution)* resolution
            xn = np.append(xn, xn[-1]+fitX)
            yn = np.append(yn, yn[-1])
            zn = np.append(zn, zn[-1])
            xn = np.append(xn, xn[-1])
            yn = np.append(yn, yn[-1])
            zn = np.append(zn, zn[-1]+fitZ)

    # check last point
    dx = x[-1]-xn[-1]
    dy = y[-1]-yn[-1]
    dz = z[-1]-zn[-1]

    if np.abs(dx) or np.abs(dy) or np.abs(dz) >= resolution:
        fitX = round((x[-1]-xn[-1])/resolution)*resolution
        fitY = round((y[-1]-yn[-1])/resolution)*resolution
        fitZ = round((z[-1]-zn[-1])/resolution)*resolution
        xn = np.append(xn, xn[-1]+fitX)
        yn = np.append(yn, yn[-1]+fitY)
        zn = np.append(zn, zn[-1]+fitZ)    

    # plt.plot(xn, ys)
    # plt.axis([0, 220, 0, 120])
    # plt.show()

    return xn, yn, zn

# L           = 0.2               # m
# L_plate     = 0.07
# resolution  = 0.0005            # m
# R           = 0.019978589752617
# Rside       = 0.011
# B           = 0.17                   # m
# tol3d       = 0.0003
# G           = 0.0023 + tol3d    # m
# arcRadius   = 0.025            # m
# W1          = 0.13              # m
# wfeed       = 0.011 + tol3d          # m
# C1          = ((W1*1e3/2) - (G*1e3/2))/(np.exp(R*L*1e3)-np.exp(R*0))
# C1_side     = (B*1e3/2-wfeed*1e3/2)/(np.exp(Rside*L*1e3)-np.exp(Rside*0))
# C2          = (G*1e3/2 * np.exp(R*L*1e3)-W1*1e3/2 * np.exp(R*0))/(np.exp(R*L*1e3)-np.exp(R*0))  # 0.259141  ( G / 2 mm * exp(R * L / 1 mm) - W1 / 2 mm * exp(0 oE) ) / ( exp(R * L / 1 mm) - exp(0 oE) )
# C2_side     = (wfeed*1e3/2*np.exp(Rside*L*1e3)-B*1e3/2*np.exp(Rside*0))/(np.exp(Rside*L*1e3)-np.exp(Rside*0))
# slopeAngel  = np.arctan(C1*R*np.exp(R*L*1e3))  # 52.291047
# arcAngle    = np.deg2rad(90)                # deg
# arcStart    = (slopeAngel - arcAngle)       # deg
# arcStop     = arcAngle
# arcDelta    = arcStop - arcStart
# Lfeed       = 0.02                  # m
# deltaB      = 0.02                  # m
# B2          = B + deltaB            # m
# lBalun      = 0.014                 # m
# balunDiaBig = 0.011                 # m
# balunDiaSmall = 0.008               # m
# smaDia      = 0.001
# smaTeflonDia= 0.005
# smaSocketDia= 0.008
# smaScrwDia  = 0.006
# sourceresistance = 200              # ohm

# print('C1:'+str(C1)+' C1side:'+str(C1_side)+' C2:'+str(C2)+' C2side:'+str(C2_side) + ' SlopeAngel:' + str(np.rad2deg(slopeAngel))+'\n'+'ArcStart:'+ str(np.rad2deg(arcStart)))
# zl = np.arange(0, (L+resolution)*1e3, resolution*1e3)
# alpha = np.linspace(arcStart, arcStop, num=200, endpoint=True)
# # horn
# x_z = C1 * np.exp((zl*R))+C2      # horn part
# y_z = C1_side*np.exp(Rside*zl)+C2_side+(wfeed*1e3/2)-wfeed*1e3/2   # c1_side*efk^(R_side*v*u)+c2_side+(w_feed/2*v)-w_feed/2 # C1_SIDE*exp(R_SIDE*t)+C2_SIDE+(W_FEED/2mm)-W_FEED/2
# x_alpha = W1*1e3/2+arcRadius*1e3*np.sin(alpha)+np.cos(slopeAngel)*arcRadius*1e3
# y_alpha = B*1e3/2+deltaB*1e3/2*(alpha-arcStart)/arcDelta #B/2+(DELTA_B)/2*(t-ARC_START/1grd)/(ARC_DELTA/1grd)
# z_alpha = L*1e3+arcRadius*1e3*np.cos(alpha)-np.sin(slopeAngel)*arcRadius*1e3

# # discret funcion
# zn, yn_z, xn_z = disGeometryGprMax(zl, y_z, x_z, resolution*1e3)
# # zzx, xx_z = disGeometryGprMax(zl, x_z, resolution*1e3)
# za, ya, xa = disGeometryGprMax(z_alpha, y_alpha, x_alpha, resolution*1e3)
# # zy_a, y_za = disGeometryGprMax(z_alpha, y_alpah, resolution*1e3)

# # build geometry

# # zz = np.append(zzy, zzx)
# # zz = np.sort(zz)
# # print('zzy:'+str(zzy)+'\n zzx'+str(zzx)+'\n zconnect and sorted:'+str(np.unique(zz)))

# plt.plot(zn, yn_z)
# plt.show()
# plt.plot(zn, xn_z)
# plt.show()

# fig = plt.figure()
# ax = fig.gca(projection='3d')
# #plt.plot(zn, yn_z, xn_z)
# #plt.show()
# #plt.plot(z_alpha, y_alpha, x_alpha)
# plt.plot(za, ya, xa)
# # ax.set_xlim3d(0,50)
# # ax.set_ylim3d(0,20)
# # ax.set_zlim3d(0,30)


# # zreal = z-zzx/1e3
# # xx_zreal = x + xx_z/1e3
# # plt.plot(zzx, xx_z, zx_a, x_za, zzy, yy_z, zy_a, y_za)
# # plt.axis('equal')
# #plt.axis([0, 220, 0, 120])
# # plt.plot(zreal, xx_zreal)
# plt.show()