from __future__ import unicode_literals

from django.db import models
import decimal
from decimal import *
import math

class measurements(models.Model):
	neck_to_bust = models.DecimalField(max_digits=5, decimal_places=3)
	shoulders = models.DecimalField(max_digits=5, decimal_places=3)
	bust = models.DecimalField(max_digits=5, decimal_places=3)
	underbust = models.DecimalField(max_digits=5, decimal_places=3)
	underarm_to_waist = models.DecimalField(max_digits=5, decimal_places=3)
	underbust_to_waist = models.DecimalField(max_digits=5, decimal_places=3)
	waist =  models.DecimalField(max_digits=5, decimal_places=3)
	waist_to_hip = models.DecimalField(max_digits=5, decimal_places=3)
	hip = models.DecimalField(max_digits=5, decimal_places=3)
	hip_to_knee = models.DecimalField(max_digits=5, decimal_places=3)
	hip_to_ankle = models.DecimalField(max_digits=5, decimal_places=3)

	def __unicode__(self):
		getcontext().prec = 3
		shouldersX = (self.shoulders/4)*10
		neckX = shouldersX/3
		neckY = shouldersX/3
		shouldersY1 = (self.neck_to_bust/2)*5+neckY
		shouldersY2 = (self.neck_to_bust)*5+shouldersY1
		bustX = (self.underbust/4)*10 #self.bust/4 - shouldersX
		bustY = (self.neck_to_bust)*10+neckY
		underbustX = (self.underbust/4)*10
		underbustY = (self.underarm_to_waist - self.underbust_to_waist)*10+bustY
		waistX = (self.waist/4)*10
		waistY = (self.underbust_to_waist)*10+underbustY
		hipX = (self.hip/4)*10
		hipY = (self.waist_to_hip)*10+waistY
		#crotchX = 
		#crotchY =
		kneeX = (self.hip + self.waist)/8*10
		kneeY = (self.hip_to_knee)*5+hipY

		shoulders1_curve = "C %s %s, %s %s, %s %s" % (neckX*4/3, neckY*4/3, shouldersX - neckX/3, shouldersY1- neckY/3, shouldersX, shouldersY1)
		shoulders2_curve = "S %s %s, %s %s" % (shouldersX+neckX/3, (2*shouldersY2+shouldersY1)/3,shouldersX, shouldersY2)
		bust_curve = "S %s %s, %s %s" % (bustX, bustY, bustX, bustY)
		underbust_curve = "S %s %s, %s %s" % (underbustX + (bustX-underbustX)/2, underbustY + (bustY-underbustY)/2, underbustX, underbustY)
		waist_curve = "S %s %s, %s %s" % (waistX + (underbustX- waistX)/3, waistY + (underbustY - waistY)/5, waistX, waistY)
		hip_curve = "S %s %s, %s %s" % (hipX + (waistX-hipX)/3, hipY + (waistY-hipY)/2, hipX, hipY)
		knee_curve = "S %s %s, %s %s" % (kneeX, kneeY, kneeX, kneeY)

		shoulders1_curve_2 = "C %s %s, %s %s, %s %s" % (0-(neckX*4/3), neckY*4/3, 0-(shouldersX - neckX/3), shouldersY1- neckY/3, 0-(shouldersX), shouldersY1)
		shoulders2_curve_2 = "S %s %s, %s %s" % (0-(shouldersX+neckX/3), (2*shouldersY2+shouldersY1)/3,0-(shouldersX), shouldersY2)
		bust_curve_2 = "S %s %s, %s %s" % (0-(bustX), bustY, 0-bustX, bustY)
		underbust_curve_2 = "S %s %s, %s %s" % (0-(underbustX) + (bustX-underbustX)/2, underbustY + (bustY-underbustY)/2, 0-(underbustX), underbustY)
		waist_curve_2 = "S %s %s, %s %s" % (0-(waistX) + (underbustX- waistX)/3, waistY + (underbustY - waistY)/5, 0-(waistX), waistY)
		hip_curve_2 = "S %s %s, %s %s" % (0-(hipX + (waistX-hipX)/3), hipY + (waistY-hipY)/2, 0-(hipX), hipY)
		knee_curve_2 = "S %s %s, %s %s" % (0-(kneeX), kneeY, 0-(kneeX), kneeY)

		return u"m 0,0 L %s,0 l 0,%s %s %s %s %s %s %s %s L 0,%s M 0,0 l %s,0 l 0,%s %s %s %s %s %s %s %s l %s,0, M 10,%s L 10,%s L 35,%s L 35,%s Q 0,%s -35,%s L -35,%s L -10,%s L-10,%s" % (neckX, neckY, shoulders1_curve, shoulders2_curve, bust_curve, underbust_curve, waist_curve, hip_curve, knee_curve, kneeY, 0-neckX, neckY, shoulders1_curve_2, shoulders2_curve_2, bust_curve_2, underbust_curve_2, waist_curve_2, hip_curve_2, knee_curve_2, kneeX, kneeY, kneeY+230, kneeY+250, kneeY+260, kneeY+275, kneeY+260, kneeY+250, kneeY+230, kneeY)
		#return u"m 0,0 l 30,0 l %s,%s l %s,%s l %s,%s l %s,%s l %s,%s l %s,%s l %s,%s" % (neckX, neckY, shouldersX, shouldersY, bustX, bustY, underbustX, underbustY, waistX, waistY, hipX, hipY, kneeX, kneeY)


class pattern(models.Model):
	

	full_length = models.DecimalField(max_digits=5, decimal_places=3)#shoulder at neck to waist line
	center_front_length = models.DecimalField(max_digits=5, decimal_places=3)#hollow at center front neck to waist line
	shoulder_tip = models.DecimalField(max_digits=5, decimal_places=3)
	shoulder_length = models.DecimalField(max_digits=5, decimal_places=3)
	across_shoulder = models.DecimalField(max_digits=5, decimal_places=3)
	armhole_depth = models.DecimalField(max_digits=5, decimal_places=3)
	bust_depth = models.DecimalField(max_digits=5, decimal_places=3)#shoulder tip to bust point (bust point is the nipple. To find, poke a needle from INSIDE of bra/tank top to OUTSIDE and mark
	bust_span = models.DecimalField(max_digits=5, decimal_places=3)#bust point to bust point, divided by 2
	bust_arc = models.DecimalField(max_digits=5, decimal_places=3)#CF to bust point to armhole depth/side seam
	shoulder_slope = models.DecimalField(max_digits=5, decimal_places=3)#CF waist line to shoulder tip
	side_seam_length = models.DecimalField(max_digits=5, decimal_places=3)#armhole depth to waist line
	waist_arc = models.DecimalField(max_digits=5, decimal_places=3)#CF to SS along waist line
	dart_placement = models.DecimalField(max_digits=5, decimal_places=3)
	short = models.BooleanField() 
	
	def __unicode__(self):
		getcontext().prec = 7
		ax = 0
		ay = 0
		bx = 0
		by = self.full_length
		cx = self.across_shoulder
		cy = 0
		dx = 0
		dy = self.full_length - self.center_front_length + Decimal(0.125)
		ex = self.across_shoulder
		ey = self.full_length - Decimal(math.sqrt((pow(self.shoulder_slope, 2)-pow(cx, 2))))
		fx = Decimal(math.sqrt(pow(self.shoulder_length, 2)-pow(cy, 2)))
		fy = 0
		gx = dy
		gy = dy/(Decimal(math.tan(Decimal(math.pi)/2 + Decimal(math.atan(ey/(ex-fx))))))
		hx = gx - 1/(Decimal(math.sqrt(2)))*2
		hy = gy - 1/(Decimal(math.sqrt(2)))*2
		ix = self.across_shoulder
		iy = ey + self.armhole_depth
		jx = self.across_shoulder
		if self.short:
			jy = iy + 1
		else:
			jy = iy + 2
		kx = self.across_shoulder
		ky = self.armhole_depth / 2
		lx = 0
		ly = ky
		mx = kx - 1/2
		my = ky
		nx = ex - Decimal(math.cos( math.atan((by-ey) / (bx-ex))))* self.bust_depth
		ny = ey + Decimal(math.sin( -math.atan((by-ey) / (bx-ex))))* self.bust_depth
		ox = 0
		oy = ny
		px = self.bust_span
		py = oy
		qx = px+Decimal(math.sqrt(pow(self.bust_arc - self.bust_span, 2)-pow(oy-jy, 2)))
		qy = jy
		rx = self.bust_span+Decimal(math.sqrt(Decimal(pow(math.sqrt(pow(py-qy,2)+pow(px-qx,2)),2)) - pow(iy - py,2)))
		ry = iy
		sx = rx+Decimal(math.cos( Decimal(math.atan((qy-ry) / (qx-rx)))))* self.side_seam_length
		sy = ry+Decimal(math.sin( Decimal(math.atan((qy-ry) / (qx-rx)))))* self.side_seam_length
		tx = rx+Decimal(math.cos( Decimal(math.atan((qy-ry) / (qx-rx)))))* Decimal(0.5)
		ty = ry+Decimal(math.sin( Decimal(math.atan((qy-ry) / (qx-rx)))))* Decimal(0.5)
		ux = self.dart_placement
		uy = by
		vx = ux+Decimal(math.cos( math.atan(-(uy-py) / (ux-px)))*3/16)
		vy = uy+Decimal(math.sin( math.atan(-(uy-py) / (ux-px)))*3/16)
		wx = sx - (self.waist_arc - self.dart_placement)*Decimal(math.cos( Decimal(math.atan((vy-sy) / (vx-sx)))))
		wy = sy - (self.waist_arc - self.dart_placement)*Decimal(math.sin( Decimal(math.atan((vy-sy) / (vx-sx)))))
		xx = px + Decimal( math.cos( Decimal(math.atan((wy-py) / (wx-px))))) * Decimal(math.sqrt(pow(py-vy,2)+pow(px-vx,2)))
		xy = py + Decimal( math.sin( Decimal(math.atan((wy-py) / (wx-px))))) * Decimal(math.sqrt(pow(py-vy,2)+pow(px-vx,2)))
		print str(vx-ux) + "vx"
		print str(vy-uy) + "vy"
		yx = Decimal(1/8)
		yy = Decimal(1/8)
		return u"M %s,%s L %s,%s L %s,%s L %s,%s L %s,%s L %s,%s L %s,%s L %s,%s L %s,%s L %s,%s Z" % (bx, by, dx, dy, fx, fy, ex, ey, mx, my, tx, ty, sx, sy, xx, xy, px, py, vx, vy)
		
