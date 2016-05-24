from __future__ import unicode_literals

from django.db import models
import decimal
from decimal import *

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

		