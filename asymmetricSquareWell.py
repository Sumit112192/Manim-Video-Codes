from manim import *
import numpy as np
#Size of the screen: 8 x 14
# class InfinteWell(Scene):
# 	def construct(self):
# 		axes = NumberLine(
# 			x_range = [-4.9, 9.9, 5],
# 			include_ticks = True,
# 			length = 10,
# 			numbers_with_elongated_ticks = [0, 5]
# 			).shift(DOWN)
# 		self.add(axes)
# 		print(axes.n2p(0))
# 		line1 = Line(start = [axes.n2p(0)[0], 3, 0], end = [axes.n2p(0)[0], -3, 0])
# 		line2 = Line(start = [axes.n2p(5)[0], 3, 0], end = [axes.n2p(5)[0], -3, 0])
# 		self.add(line1, line2)

topic = "Infinte Potential Well"
class Intro(Scene):
	def construct(self):
		introText = Text(topic, color = BLUE).scale(1.5)
		self.play(Write(introText))

		headingText = Text(topic, color=BLUE).align_on_border(UP)
		self.play(introText.animate.become(headingText))


class InfiniteWell(Scene):
	def construct(self):
		headingText = Text(topic, color=BLUE).align_on_border(UP)
		self.add(headingText)
		leftAxes = Line(start = (-6, 0, 0), end = (-2, 0, 0))
		rightAxes = Line(start = (2, 0, 0), end = (6, 0, 0))

		self.play(Create(leftAxes))
		self.play(Create(rightAxes))

		leftVerticalLine = Line(start = (-2, 2.5, 0), end = (-2, -2.5, 0))
		rightVerticalLine = Line(start = (2, 2.5, 0), end = (2, -2.5, 0))
		self.play(Create(leftVerticalLine), Create(rightVerticalLine))

		leftCurved = Line(start = (-2, 2.5, 0), end = (-2-1/(2)**(0.5), 2.5-1/2**(0.5), 0))
		leftCurvedGroup = VGroup()
		leftCurvedGroup.add(leftCurved)
		for i in range(9):
			leftCurvedGroup.add(leftCurved.copy().shift(DOWN/2*(i+1)))
		self.play(Create(leftCurvedGroup))

		rightCurved = Line(start = (2, 2.5, 0), end = (2+1/(2)**(0.5), 2.5-1/2**(0.5), 0))
		rightCurvedGroup = VGroup()
		rightCurvedGroup.add(rightCurved)
		for i in range(9):
			rightCurvedGroup.add(rightCurved.copy().shift(DOWN/2*(i+1)))
		self.play(Create(rightCurvedGroup))

		leftCoordinate = Tex("$x = 0$").move_to((-2, -3, 0))
		self.play(Write(leftCoordinate))

		rightCoordinate = Tex("$x = L$").move_to((2, -3, 0))
		self.play(Write(rightCoordinate))

		V_0 = Tex("$V=0$")
		self.play(Write(V_0))

		V_infinity = Tex(r"$V=\infty$").move_to((-4, 1.5, 0))
		V_right = V_infinity.copy().move_to((4, 1.5, 0))
		self.play(Write(V_infinity), Write(V_right))
		self.wait()

		self.play(FadeOut(headingText, leftAxes, rightAxes, leftVerticalLine, rightVerticalLine, leftCurvedGroup, rightCurvedGroup,
			leftCoordinate, rightCoordinate, V_0, V_infinity, V_right), run_time = 2)


class EnergyEigenState(Scene):
	def construct(self):
		tname = "Energy Eigen State and Energy"
		introText = Text(tname, color = BLUE).scale(1.5)
		self.play(Write(introText))

		headingText = Text(tname, color=BLUE).align_on_border(UP)
		self.play(introText.animate.become(headingText))

		state = r"$\phi_n(x) = \sqrt{\frac{2}{L}}\sin (\frac{n\pi x}{L})$"
		stateText = Tex(state, color = BLUE).scale(1.5)
		self.play(Write(stateText))

		energy = r"with $E = \frac{n^2h^2}{2mL^2}$"
		energyTex = Tex(energy, color = BLUE).scale(1.5).next_to(stateText, DOWN)
		self.play(Write(energyTex))

		self.play(FadeOut(stateText, energyTex))

		# note = Text("Note", color = RED).scale(1).next_to(headingText, DOWN+2.5*LEFT)
		# self.add(note)

		firstPoint = BulletedList("Since the wave function is complex, we would be plotting the real part of wave function", color = BLUE).next_to(headingText, 2.5*DOWN).scale(0.8)
		self.play(Write(firstPoint))
		self.wait()
		self.play(FadeOut(introText, firstPoint))
		self.wait()

class GroundState(Scene):
	def construct(self):
		tname = "Ground State"
		introText = Text(tname, color = BLUE).scale(1.5)
		self.play(Write(introText))

		headingText = Text(tname, color=BLUE).align_on_border(UP)
		self.play(introText.animate.become(headingText))

class GroundData(Scene):
	def construct(self):
		tname = "Ground State"
		headingText = Text(tname, color=BLUE).align_on_border(UP)
		self.add(headingText)

		backgroundColor = "#274c43"
		box1 = Polygon([-6, 2.5, 0], [-1, 2.5, 0], [-1, -2, 0], [-6, -2, 0], fill_color = backgroundColor, fill_opacity = 1)
		self.add(box1)

		box2 = Polygon([1, 2.5, 0], [6, 2.5, 0], [6, -2, 0], [1, -2, 0], fill_color = backgroundColor, fill_opacity = 1)
		self.add(box2)


		phi_1 = Tex(r"$\phi_1(x, 0) = \sqrt{\frac{2}{L}}\sin(\frac{\pi x}{L})$")
		phi_1t = Tex(r"$\phi_1(x, t) = \sqrt{\frac{2}{L}}\sin(\frac{\pi x}{L})e^{-i\frac{E_1}{\hbar}t}$").next_to(phi_1, DOWN)
		Realphi_1t = Tex(r"Real($\phi_1(x, t)) = \sqrt{\frac{2}{L}}\sin(\frac{\pi x}{L})\cos(\frac{E_1}{\hbar}t)$").next_to(phi_1t, DOWN)

		leftData = VGroup(phi_1, phi_1t, Realphi_1t).next_to(box1, 0*DOWN).scale(0.5)
		self.add(leftData)


		P_1 =  Tex(r"$\mathbb{P}(x, 0) = |\phi_1^*(x, 0)\phi_1(x, 0)|= \frac{2}{L}\sin^2(\frac{\pi x}{L})$")
		P_1t = Tex(r"$\mathbb{P}(x, t) = |\phi_1^*(x, t)\phi_1(x, t)|= \frac{2}{L}\sin^2(\frac{\pi x}{L})$").next_to(P_1, DOWN)
		PIndependent = Text(r"Independent of time").next_to(P_1t, DOWN)

		rightData = VGroup(P_1, P_1t, PIndependent).next_to(box2, 0*DOWN).scale(0.5)
		self.add(rightData)


		baseLeftData = Tex(r"$\phi_1$").next_to(box1, DOWN)
		self.play(leftData.animate.become(baseLeftData))

		baseRightData = Tex(r"$\mathbb{P} = |\phi_1^*\phi_1|$").next_to(box2, DOWN)
		self.play(rightData.animate.become(baseRightData))
		self.wait()
		#self.wait()	

class GroundAnimation(Scene):
	def construct(self):
		tname = "Ground State"
		headingText = Text(tname, color=BLUE).align_on_border(UP)
		self.add(headingText)

		backgroundColor = "#274c43"
		box1 = Polygon([-6, 2.5, 0], [-1, 2.5, 0], [-1, -2, 0], [-6, -2, 0], fill_color = backgroundColor, fill_opacity = 1)
		self.add(box1)

		box2 = Polygon([1, 2.5, 0], [6, 2.5, 0], [6, -2, 0], [1, -2, 0], fill_color = backgroundColor, fill_opacity = 1)
		self.add(box2)
		baseLeftData = Tex(r"$\phi_1$").next_to(box1, DOWN)
		baseRightData = Tex(r"$\mathbb{P} = |\phi_1^*\phi_1|$").next_to(box2, DOWN)

		self.add(baseLeftData, baseRightData)
		axes = Axes(x_length = 5, x_range= [-0.1, 1.1, 1], y_length = 4.5, y_range = [-2, 2, 2], tips = False)
		axes1 = axes.copy().shift(3.5*LEFT+0.25*UP)
		self.add(axes1)

		axes2 = axes.copy().shift(3.5*RIGHT+0.25*UP)
		self.add(axes2)
		baseLine = Line(start = [0, -2, 0], end = [0, 2.5, 0], color = BLACK)
		l1 = baseLine.copy().shift(axes1.c2p([0, 0, 0])[0]*RIGHT)
		self.add(l1)

		l2 = baseLine.copy().shift(axes1.c2p([1, 0, 0])[0]*RIGHT)
		self.add(l2)

		l3 = baseLine.copy().shift(axes2.c2p([0, 0, 0])[0]*RIGHT)
		self.add(l3)

		l4 = baseLine.copy().shift(axes2.c2p([1, 0, 0])[0]*RIGHT)
		self.add(l4)
		t = ValueTracker(0)
		leftBaseFunction = axes1.plot(lambda x: (2-0.1)**(0.5)*np.sin(np.pi*x), x_range = [0, 1, 0.01], color = BLUE)
		self.add(leftBaseFunction)


		rightBaseFunction = axes2.plot(lambda x: (2-0.1)*np.sin(np.pi*x)*np.sin(np.pi*x), x_range = [0, 1, 0.01], color = BLUE)
		self.add(rightBaseFunction)

		leftBaseFunction.add_updater(lambda mobject: mobject.become(axes1.plot(lambda x: (2-0.1)**(0.5)*np.sin(np.pi*x)*np.cos(t.get_value()), x_range = [0, 1, 0.01], color = BLUE)))
		self.play(t.animate.set_value(10), run_time = 10, rate_func = linear)

		

		# leftBaseFunction.add_updater(lambda mobject: mobject.become(axes1.plot(lambda x: (2-0.1)**(0.5)*np.sin(np.pi*x)*np.cos(t.get_value()), x_range = [0, 1, 0.01])))
		# self.play(t.animate.set_value(10), run_time = 10, rate_func = linear)
		



########First Excited State #########################

class FirstState(Scene):
	def construct(self):
		tname = "First Excited State"
		introText = Text(tname, color = BLUE).scale(1.5)
		self.play(Write(introText))

		headingText = Text(tname, color=BLUE).align_on_border(UP)
		self.play(introText.animate.become(headingText))

class FirstData(Scene):
	def construct(self):
		tname = "First Excited State"
		headingText = Text(tname, color=BLUE).align_on_border(UP)
		self.add(headingText)

		backgroundColor = "#274c43"
		box1 = Polygon([-6, 2.5, 0], [-1, 2.5, 0], [-1, -2, 0], [-6, -2, 0], fill_color = backgroundColor, fill_opacity = 1)
		self.add(box1)

		box2 = Polygon([1, 2.5, 0], [6, 2.5, 0], [6, -2, 0], [1, -2, 0], fill_color = backgroundColor, fill_opacity = 1)
		self.add(box2)


		phi_1 = Tex(r"$\phi_2(x, 0) = \sqrt{\frac{2}{L}}\sin(\frac{2\pi x}{L})$")
		phi_1t = Tex(r"$\phi_2(x, t) = \sqrt{\frac{2}{L}}\sin(\frac{2\pi x}{L})e^{-i\frac{E_2}{\hbar}t}$").next_to(phi_1, DOWN)
		Realphi_1t = Tex(r"Real($\phi_2(x, t)) = \sqrt{\frac{2}{L}}\sin(\frac{2\pi x}{L})\cos(\frac{E_2}{\hbar}t)$").next_to(phi_1t, DOWN)

		leftData = VGroup(phi_1, phi_1t, Realphi_1t).next_to(box1, 0*DOWN).scale(0.5)
		self.add(leftData)


		P_1 =  Tex(r"$\mathbb{P}(x, 0) = |\phi_2^*(x, 0)\phi_2(x, 0)|= \frac{2}{L}\sin^2(\frac{2\pi x}{L})$")
		P_1t = Tex(r"$\mathbb{P}(x, t) = |\phi_2^*(x, t)\phi_2(x, t)|= \frac{2}{L}\sin^2(\frac{2\pi x}{L})$").next_to(P_1, DOWN)
		PIndependent = Text(r"Independent of time").next_to(P_1t, DOWN)

		rightData = VGroup(P_1, P_1t, PIndependent).next_to(box2, 0*DOWN).scale(0.5)
		self.add(rightData)


		baseLeftData = Tex(r"$\phi_2$").next_to(box1, DOWN)
		self.play(leftData.animate.become(baseLeftData))

		baseRightData = Tex(r"$\mathbb{P} = |\phi_2^*\phi_2|$").next_to(box2, DOWN)
		self.play(rightData.animate.become(baseRightData))
		self.wait()
		#self.wait()	

class FirstAnimation(Scene):
	def construct(self):
		tname = "First Excited State"
		headingText = Text(tname, color=BLUE).align_on_border(UP)
		self.add(headingText)

		backgroundColor = "#274c43"
		box1 = Polygon([-6, 2.5, 0], [-1, 2.5, 0], [-1, -2, 0], [-6, -2, 0], fill_color = backgroundColor, fill_opacity = 1)
		self.add(box1)

		box2 = Polygon([1, 2.5, 0], [6, 2.5, 0], [6, -2, 0], [1, -2, 0], fill_color = backgroundColor, fill_opacity = 1)
		self.add(box2)
		baseLeftData = Tex(r"$\phi_2$").next_to(box1, DOWN)
		baseRightData = Tex(r"$\mathbb{P} = |\phi_2^*\phi_2|$").next_to(box2, DOWN)

		self.add(baseLeftData, baseRightData)
		axes = Axes(x_length = 5, x_range= [-0.1, 1.1, 1], y_length = 4.5, y_range = [-2, 2, 2], tips = False)
		axes1 = axes.copy().shift(3.5*LEFT+0.25*UP)
		self.add(axes1)

		axes2 = axes.copy().shift(3.5*RIGHT+0.25*UP)
		self.add(axes2)
		baseLine = Line(start = [0, -2, 0], end = [0, 2.5, 0], color = BLACK)
		l1 = baseLine.copy().shift(axes1.c2p([0, 0, 0])[0]*RIGHT)
		self.add(l1)

		l2 = baseLine.copy().shift(axes1.c2p([1, 0, 0])[0]*RIGHT)
		self.add(l2)

		l3 = baseLine.copy().shift(axes2.c2p([0, 0, 0])[0]*RIGHT)
		self.add(l3)

		l4 = baseLine.copy().shift(axes2.c2p([1, 0, 0])[0]*RIGHT)
		self.add(l4)
		t = ValueTracker(0)
		leftBaseFunction = axes1.plot(lambda x: (2-0.1)**(0.5)*np.sin(2*np.pi*x), x_range = [0, 1, 0.01], color = BLUE)
		self.add(leftBaseFunction)


		rightBaseFunction = axes2.plot(lambda x: (2-0.1)*np.sin(2*np.pi*x)*np.sin(2*np.pi*x), x_range = [0, 1, 0.01], color = BLUE)
		self.add(rightBaseFunction)

		leftBaseFunction.add_updater(lambda mobject: mobject.become(axes1.plot(lambda x: (2-0.1)**(0.5)*np.sin(2*np.pi*x)*np.cos(4*t.get_value()), x_range = [0, 1, 0.01], color = BLUE)))
		self.play(t.animate.set_value(10), run_time = 10, rate_func = linear)



#####SuperPosition of States############

class SuperPositionState(Scene):
	def construct(self):
		tname = "Superposition of States"
		introText = Text(tname, color = BLUE).scale(1.5)
		self.play(Write(introText))

		headingText = Text(tname, color=BLUE).align_on_border(UP)
		self.play(introText.animate.become(headingText))

class SuperPositionData(Scene):
	def construct(self):
		tname = "Superposition of States"
		headingText = Text(tname, color=BLUE).align_on_border(UP)
		self.add(headingText)

		backgroundColor = "#274c43"
		box1 = Polygon([-6, 2.5, 0], [-1, 2.5, 0], [-1, -2, 0], [-6, -2, 0], fill_color = backgroundColor, fill_opacity = 1)
		self.add(box1)

		box2 = Polygon([1, 2.5, 0], [6, 2.5, 0], [6, -2, 0], [1, -2, 0], fill_color = backgroundColor, fill_opacity = 1)
		self.add(box2)


		phi_1 = Tex(r"$\psi(x, 0) = \frac{1}{\sqrt{2}}\phi_1+\frac{1}{\sqrt{2}}\phi_2$")
		phi_1t = Tex(r"$\psi(x, t) = \frac{1}{\sqrt{2}}\phi_1e^{-i\frac{E_1}{\hbar}t}+\frac{1}{\sqrt{2}}\phi_2e^{-i\frac{E_2}{\hbar}t}$").next_to(phi_1, DOWN)
		Realphi_1t = Tex(r"\begin{equation*} \begin{split} \text{Real}(\psi(x, t)) = & \frac{1}{\sqrt{2}}\phi_1\cos(\frac{E_1}{\hbar}t)\\&+\frac{1}{\sqrt{2}}\phi_2\cos(\frac{E_2}{\hbar}t) \end{split} \end{equation*}").next_to(phi_1t, DOWN)

		leftData = VGroup(phi_1, phi_1t, Realphi_1t).next_to(box1, 0*DOWN).scale(0.5)
		self.add(leftData)


		P_1 =  Tex(r"\begin{equation*} \begin{split} \mathbb{P}(x, 0) = & |\psi^*(x, 0)\psi(x, 0)| = \frac{1}{2}\phi_1^2+\frac{1}{2}\phi_2^2+\\ & \phi_1\phi_2 \end{split} \end{equation*}")
		P_1t = Tex(r"\begin{equation*} \begin{split} \mathbb{P}(x, t) = & |\psi^*(x, t)\psi(x, t)| = \frac{1}{2}\phi_1^2+\frac{1}{2}\phi_2^2+\\ & \phi_1\phi_2\cos(\frac{(E_1-E_2)}{\hbar}t) \end{split} \end{equation*}").next_to(P_1, DOWN)
		PIndependent = Text(r"Dependent of time").next_to(P_1t, DOWN)

		rightData = VGroup(P_1, P_1t, PIndependent).next_to(box2, 0*DOWN).scale(0.5)
		self.add(rightData)


		baseLeftData = Tex(r"$\psi$").next_to(box1, DOWN)
		self.play(leftData.animate.become(baseLeftData))

		baseRightData = Tex(r"$\mathbb{P} = |\psi^*\psi|$").next_to(box2, DOWN)
		self.play(rightData.animate.become(baseRightData))
		self.wait()
		#self.wait()	

class SuperPositionAnimation(Scene):
	def construct(self):
		tname = "Superposition of States"
		headingText = Text(tname, color=BLUE).align_on_border(UP)
		self.add(headingText)

		backgroundColor = "#274c43"
		box1 = Polygon([-6, 2.5, 0], [-1, 2.5, 0], [-1, -2, 0], [-6, -2, 0], fill_color = backgroundColor, fill_opacity = 1)
		self.add(box1)

		box2 = Polygon([1, 2.5, 0], [6, 2.5, 0], [6, -2, 0], [1, -2, 0], fill_color = backgroundColor, fill_opacity = 1)
		self.add(box2)
		baseLeftData = Tex(r"$\psi$").next_to(box1, DOWN)
		baseRightData = Tex(r"$\mathbb{P} = |\psi^*\psi_2|$").next_to(box2, DOWN)

		self.add(baseLeftData, baseRightData)
		axes = Axes(x_length = 5, x_range= [-0.1, 1.1, 1], y_length = 4.5, y_range = [-6, 6, 2], tips = False)
		axes1 = axes.copy().shift(3.5*LEFT+0.25*UP)
		self.add(axes1)

		axes2 = axes.copy().shift(3.5*RIGHT+0.25*UP)
		self.add(axes2)
		baseLine = Line(start = [0, -2, 0], end = [0, 2.5, 0], color = BLACK)
		l1 = baseLine.copy().shift(axes1.c2p([0, 0, 0])[0]*RIGHT)
		self.add(l1)

		l2 = baseLine.copy().shift(axes1.c2p([1, 0, 0])[0]*RIGHT)
		self.add(l2)

		l3 = baseLine.copy().shift(axes2.c2p([0, 0, 0])[0]*RIGHT)
		self.add(l3)

		l4 = baseLine.copy().shift(axes2.c2p([1, 0, 0])[0]*RIGHT)
		self.add(l4)
		t = ValueTracker(0)
		leftBaseFunction = axes1.plot(lambda x: (2-0.1)**(0.5)*np.sin(np.pi*x)+(2-0.1)**(0.5)*np.sin(2*np.pi*x), x_range = [0, 1, 0.01], color = BLUE)
		self.add(leftBaseFunction)


		rightBaseFunction = axes2.plot(lambda x: (2-0.1)*np.sin(np.pi*x)*np.sin(np.pi*x)+(2-0.1)*np.sin(2*np.pi*x)*np.sin(2*np.pi*x) + (2-0.1)**(0.5)*np.sin(np.pi*x)*(2-0.1)**(0.5)*np.sin(2*np.pi*x), x_range = [0, 1, 0.01], color = BLUE)
		self.add(rightBaseFunction)

		leftBaseFunction.add_updater(lambda mobject: mobject.become(axes1.plot(lambda x: (2-0.1)**(0.5)*np.sin(np.pi*x)*np.cos(t.get_value())+(2-0.1)**(0.5)*np.sin(2*np.pi*x)*np.cos(4*t.get_value()), x_range = [0, 1, 0.01], color = BLUE)))
		rightBaseFunction.add_updater(lambda mobject: mobject.become(axes2.plot(lambda x: (2-0.1)*np.sin(np.pi*x)*np.sin(np.pi*x)+(2-0.1)*np.sin(2*np.pi*x)*np.sin(2*np.pi*x) + (2-0.1)**(0.5)*np.sin(np.pi*x)*(2-0.1)**(0.5)*np.sin(2*np.pi*x)*np.cos(3*t.get_value()), x_range = [0, 1, 0.01], color = BLUE)))
		self.play(t.animate.set_value(10), run_time = 10, rate_func = linear)


class CompleteInfinitePotentialWell(Scene):
	def construct(self):
		###Intro To Infinte Potential Well ###########
		self.next_section("Infinite Potential Well")
		topic = "Infinte Potential Well"
		introText = Text(topic, color = BLUE).scale(1.5)
		self.play(Write(introText))
		headingText = Text(topic, color=BLUE).align_on_border(UP)
		self.play(introText.animate.become(headingText))

		###Drawing of Infinte Well############
		self.next_section("Drawing of Infinite Well")

		leftAxes = Line(start = (-6, 0, 0), end = (-2, 0, 0))
		rightAxes = Line(start = (2, 0, 0), end = (6, 0, 0))

		self.play(Create(leftAxes))
		self.play(Create(rightAxes))

		leftVerticalLine = Line(start = (-2, 2.5, 0), end = (-2, -2.5, 0))
		rightVerticalLine = Line(start = (2, 2.5, 0), end = (2, -2.5, 0))
		self.play(Create(leftVerticalLine), Create(rightVerticalLine))

		leftCurved = Line(start = (-2, 2.5, 0), end = (-2-1/(2)**(0.5), 2.5-1/2**(0.5), 0))
		leftCurvedGroup = VGroup()
		leftCurvedGroup.add(leftCurved)
		for i in range(9):
			leftCurvedGroup.add(leftCurved.copy().shift(DOWN/2*(i+1)))
		self.play(Create(leftCurvedGroup))

		rightCurved = Line(start = (2, 2.5, 0), end = (2+1/(2)**(0.5), 2.5-1/2**(0.5), 0))
		rightCurvedGroup = VGroup()
		rightCurvedGroup.add(rightCurved)
		for i in range(9):
			rightCurvedGroup.add(rightCurved.copy().shift(DOWN/2*(i+1)))
		self.play(Create(rightCurvedGroup))

		leftCoordinate = Tex("$x = 0$").move_to((-2, -3, 0))
		self.play(Write(leftCoordinate))

		rightCoordinate = Tex("$x = L$").move_to((2, -3, 0))
		self.play(Write(rightCoordinate))

		V_0 = Tex("$V=0$")
		self.play(Write(V_0))

		V_infinity = Tex(r"$V=\infty$").move_to((-4, 1.5, 0))
		V_right = V_infinity.copy().move_to((4, 1.5, 0))
		self.play(Write(V_infinity), Write(V_right))
		self.wait()

		self.play(FadeOut(introText, leftAxes, rightAxes, leftVerticalLine, rightVerticalLine, leftCurvedGroup, rightCurvedGroup,
			leftCoordinate, rightCoordinate, V_0, V_infinity, V_right), run_time = 1)




		####Energy Eigen State and Energy###########
		self.next_section("Energy Eigen State and Energy")

		tname = "Energy Eigen State and Energy"
		introText = Text(tname, color = BLUE).scale(1.5)
		self.play(Write(introText))

		headingText = Text(tname, color=BLUE).align_on_border(UP)
		self.play(introText.animate.become(headingText))

		state = r"$\phi_n(x) = \sqrt{\frac{2}{L}}\sin (\frac{n\pi x}{L})$"
		stateText = Tex(state, color = BLUE).scale(1.5)
		self.play(Write(stateText))

		energy = r"with $E = \frac{n^2h^2}{8mL^2}$"
		energyTex = Tex(energy, color = BLUE).scale(1.5).next_to(stateText, DOWN)
		self.play(Write(energyTex))

		self.play(FadeOut(stateText, energyTex))

		# note = Text("Note", color = RED).scale(1).next_to(headingText, DOWN+2.5*LEFT)
		# self.add(note)

		firstPoint = BulletedList("Since the wave function is complex, we would be plotting the real part of wave function", color = BLUE).next_to(headingText, 2.5*DOWN).scale(0.8)
		self.play(Write(firstPoint))
		self.wait()
		self.play(FadeOut(introText, firstPoint), run_time = 1)
		self.wait()



		####Ground State#########
		self.next_section("Ground State")

		tname = "Ground State"
		introText = Text(tname, color = BLUE).scale(1.5)
		self.play(Write(introText))

		headingText = Text(tname, color=BLUE).align_on_border(UP)
		self.play(introText.animate.become(headingText))


		#####Ground Data############
		self.next_section("Ground Data")

		# tname = "Ground State"
		# headingText = Text(tname, color=BLUE).align_on_border(UP)
		# self.add(headingText)

		backgroundColor = "#274c43"
		box1 = Polygon([-6, 2.5, 0], [-1, 2.5, 0], [-1, -2, 0], [-6, -2, 0], fill_color = backgroundColor, fill_opacity = 1)
		self.play(DrawBorderThenFill(box1))

		box2 = Polygon([1, 2.5, 0], [6, 2.5, 0], [6, -2, 0], [1, -2, 0], fill_color = backgroundColor, fill_opacity = 1)
		self.play(DrawBorderThenFill(box2))


		phi_1 = Tex(r"$\phi_1(x, 0) = \sqrt{\frac{2}{L}}\sin(\frac{\pi x}{L})$")
		phi_1t = Tex(r"$\phi_1(x, t) = \sqrt{\frac{2}{L}}\sin(\frac{\pi x}{L})e^{-i\frac{E_1}{\hbar}t}$").next_to(phi_1, DOWN)
		Realphi_1t = Tex(r"Real($\phi_1(x, t)) = \sqrt{\frac{2}{L}}\sin(\frac{\pi x}{L})\cos(\frac{E_1}{\hbar}t)$").next_to(phi_1t, DOWN)

		leftData = VGroup(phi_1, phi_1t, Realphi_1t).next_to(box1, 0*DOWN).scale(0.5)
		self.play(Write(leftData[0]))
		self.play(Write(leftData[1]))
		self.play(Write(leftData[2]))


		P_1 =  Tex(r"$\mathbb{P}(x, 0) = |\phi_1^*(x, 0)\phi_1(x, 0)|= \frac{2}{L}\sin^2(\frac{\pi x}{L})$")
		P_1t = Tex(r"$\mathbb{P}(x, t) = |\phi_1^*(x, t)\phi_1(x, t)|= \frac{2}{L}\sin^2(\frac{\pi x}{L})$").next_to(P_1, DOWN)
		PIndependent = Text(r"Independent of time").next_to(P_1t, DOWN)

		rightData = VGroup(P_1, P_1t, PIndependent).next_to(box2, 0*DOWN).scale(0.5)
		self.play(Write(rightData[0]))
		self.play(Write(rightData[1]))
		self.play(Write(rightData[2]))


		baseLeftData = Tex(r"$\phi_1$").next_to(box1, DOWN)
		self.play(leftData.animate.become(baseLeftData))

		baseRightData = Tex(r"$\mathbb{P} = |\phi_1^*\phi_1|$").next_to(box2, DOWN)
		self.play(rightData.animate.become(baseRightData))
		self.wait()


		####Ground Animation########
		self.next_section("Ground Animation")

		axes = Axes(x_length = 5, x_range= [-0.1, 1.1, 1], y_length = 4.5, y_range = [-2, 2, 2], tips = False)
		#axes1 = axes.copy().shift(3.5*LEFT+0.25*UP)
		

		#axes2 = axes.copy().shift(3.5*RIGHT+0.25*UP)
		axes1 = axes.copy()
		axes2 = axes.copy()
		self.play(axes1.animate.shift(3.5*LEFT+0.25*UP), axes2.animate.shift(3.5*RIGHT+0.25*UP))

		baseLine = Line(start = [0, -2, 0], end = [0, 2.5, 0], color = BLACK)
		l1 = baseLine.copy().shift(axes1.c2p([0, 0, 0])[0]*RIGHT)

		l2 = baseLine.copy().shift(axes1.c2p([1, 0, 0])[0]*RIGHT)

		l3 = baseLine.copy().shift(axes2.c2p([0, 0, 0])[0]*RIGHT)

		l4 = baseLine.copy().shift(axes2.c2p([1, 0, 0])[0]*RIGHT)
	
		self.play(Create(l1), Create(l2), Create(l3), Create(l4))

		t = ValueTracker(0)
		leftBaseFunction = axes1.plot(lambda x: (2-0.1)**(0.5)*np.sin(np.pi*x), x_range = [0, 1, 0.01], color = BLUE)

		rightBaseFunction = axes2.plot(lambda x: (2-0.1)*np.sin(np.pi*x)*np.sin(np.pi*x), x_range = [0, 1, 0.01], color = BLUE)

		self.play(Create(leftBaseFunction), Create(rightBaseFunction))

		leftBaseFunction.add_updater(lambda mobject: mobject.become(axes1.plot(lambda x: (2-0.1)**(0.5)*np.sin(np.pi*x)*np.cos(t.get_value()), x_range = [0, 1, 0.01], color = BLUE)))
		self.play(t.animate.set_value(10), run_time = 10, rate_func = linear)
		leftBaseFunction.clear_updaters()
		self.play(FadeOut(axes1, axes2, l1, l2, l3, l4, leftBaseFunction, rightBaseFunction, leftData, rightData, introText, box1, box2), run_time = 2)
		#self.remove(leftBaseFunction)

		####First State##############
		self.next_section("First State")

		tname = "First Excited State"
		introText = Text(tname, color = BLUE).scale(1.5)
		self.play(Write(introText))

		headingText = Text(tname, color=BLUE).align_on_border(UP)
		self.play(introText.animate.become(headingText))


		#####First Data #############
		self.next_section("First Data")

		# tname = "First Excited State"
		# headingText = Text(tname, color=BLUE).align_on_border(UP)
		# self.add(headingText)

		backgroundColor = "#274c43"
		box1 = Polygon([-6, 2.5, 0], [-1, 2.5, 0], [-1, -2, 0], [-6, -2, 0], fill_color = backgroundColor, fill_opacity = 1)
		self.play(DrawBorderThenFill(box1))

		box2 = Polygon([1, 2.5, 0], [6, 2.5, 0], [6, -2, 0], [1, -2, 0], fill_color = backgroundColor, fill_opacity = 1)
		self.play(DrawBorderThenFill(box2))


		phi_1 = Tex(r"$\phi_2(x, 0) = \sqrt{\frac{2}{L}}\sin(\frac{2\pi x}{L})$")
		phi_1t = Tex(r"$\phi_2(x, t) = \sqrt{\frac{2}{L}}\sin(\frac{2\pi x}{L})e^{-i\frac{E_2}{\hbar}t}$").next_to(phi_1, DOWN)
		Realphi_1t = Tex(r"Real($\phi_2(x, t)) = \sqrt{\frac{2}{L}}\sin(\frac{2\pi x}{L})\cos(\frac{E_2}{\hbar}t)$").next_to(phi_1t, DOWN)

		leftData = VGroup(phi_1, phi_1t, Realphi_1t).next_to(box1, 0*DOWN).scale(0.5)
		self.play(Write(leftData[0]))
		self.play(Write(leftData[1]))
		self.play(Write(leftData[2]))


		P_1 =  Tex(r"$\mathbb{P}(x, 0) = |\phi_2^*(x, 0)\phi_2(x, 0)|= \frac{2}{L}\sin^2(\frac{2\pi x}{L})$")
		P_1t = Tex(r"$\mathbb{P}(x, t) = |\phi_2^*(x, t)\phi_2(x, t)|= \frac{2}{L}\sin^2(\frac{2\pi x}{L})$").next_to(P_1, DOWN)
		PIndependent = Text(r"Independent of time").next_to(P_1t, DOWN)

		rightData = VGroup(P_1, P_1t, PIndependent).next_to(box2, 0*DOWN).scale(0.5)
		self.play(Write(rightData[0]))
		self.play(Write(rightData[1]))
		self.play(Write(rightData[2]))


		baseLeftData = Tex(r"$\phi_2$").next_to(box1, DOWN)
		self.play(leftData.animate.become(baseLeftData))

		baseRightData = Tex(r"$\mathbb{P} = |\phi_2^*\phi_2|$").next_to(box2, DOWN)
		self.play(rightData.animate.become(baseRightData))
		self.wait()


		########First Animation############
		self.next_section("First Animation")

		# tname = "First Excited State"
		# headingText = Text(tname, color=BLUE).align_on_border(UP)
		# self.add(headingText)

		# backgroundColor = "#274c43"
		# box1 = Polygon([-6, 2.5, 0], [-1, 2.5, 0], [-1, -2, 0], [-6, -2, 0], fill_color = backgroundColor, fill_opacity = 1)
		# self.add(box1)

		# box2 = Polygon([1, 2.5, 0], [6, 2.5, 0], [6, -2, 0], [1, -2, 0], fill_color = backgroundColor, fill_opacity = 1)
		# self.add(box2)
		# baseLeftData = Tex(r"$\phi_2$").next_to(box1, DOWN)
		# baseRightData = Tex(r"$\mathbb{P} = |\phi_2^*\phi_2|$").next_to(box2, DOWN)

		# self.add(baseLeftData, baseRightData)
		axes = Axes(x_length = 5, x_range= [-0.1, 1.1, 1], y_length = 4.5, y_range = [-2, 2, 2], tips = False)
		axes1 = axes.copy()
		axes2 = axes.copy()
		self.play(axes1.animate.shift(3.5*LEFT+0.25*UP), axes2.animate.shift(3.5*RIGHT+0.25*UP))


		baseLine = Line(start = [0, -2, 0], end = [0, 2.5, 0], color = BLACK)
		l1 = baseLine.copy().shift(axes1.c2p([0, 0, 0])[0]*RIGHT)

		l2 = baseLine.copy().shift(axes1.c2p([1, 0, 0])[0]*RIGHT)

		l3 = baseLine.copy().shift(axes2.c2p([0, 0, 0])[0]*RIGHT)

		l4 = baseLine.copy().shift(axes2.c2p([1, 0, 0])[0]*RIGHT)
	
		self.play(Create(l1), Create(l2), Create(l3), Create(l4))


		t = ValueTracker(0)
		leftBaseFunction = axes1.plot(lambda x: (2-0.1)**(0.5)*np.sin(2*np.pi*x), x_range = [0, 1, 0.01], color = BLUE)

		rightBaseFunction = axes2.plot(lambda x: (2-0.1)*np.sin(2*np.pi*x)*np.sin(2*np.pi*x), x_range = [0, 1, 0.01], color = BLUE)

		self.play(Create(leftBaseFunction), Create(rightBaseFunction))

		leftBaseFunction.add_updater(lambda mobject: mobject.become(axes1.plot(lambda x: (2-0.1)**(0.5)*np.sin(2*np.pi*x)*np.cos(4*t.get_value()), x_range = [0, 1, 0.01], color = BLUE)))
		self.play(t.animate.set_value(10), run_time = 10, rate_func = linear)

		leftBaseFunction.clear_updaters()
		self.play(FadeOut(axes1, axes2, l1, l2, l3, l4, leftBaseFunction, rightBaseFunction, leftData, rightData, introText, box1, box2), run_time = 2)


		#####SuperPosition State##############
		self.next_section("Superposition of State")

		tname = "Superposition of States"
		introText = Text(tname, color = BLUE).scale(1.5)
		self.play(Write(introText))

		headingText = Text(tname, color=BLUE).align_on_border(UP)
		self.play(introText.animate.become(headingText))


		#######Superposition Data#######
		self.next_section("Superposition Data")


		backgroundColor = "#274c43"
		box1 = Polygon([-6, 2.5, 0], [-1, 2.5, 0], [-1, -2, 0], [-6, -2, 0], fill_color = backgroundColor, fill_opacity = 1)
		self.play(DrawBorderThenFill(box1))

		box2 = Polygon([1, 2.5, 0], [6, 2.5, 0], [6, -2, 0], [1, -2, 0], fill_color = backgroundColor, fill_opacity = 1)
		self.play(DrawBorderThenFill(box2))


		phi_1 = Tex(r"$\psi(x, 0) = \frac{1}{\sqrt{2}}\phi_1+\frac{1}{\sqrt{2}}\phi_2$")
		phi_1t = Tex(r"$\psi(x, t) = \frac{1}{\sqrt{2}}\phi_1e^{-i\frac{E_1}{\hbar}t}+\frac{1}{\sqrt{2}}\phi_2e^{-i\frac{E_2}{\hbar}t}$").next_to(phi_1, DOWN)
		Realphi_1t = Tex(r"\begin{equation*} \begin{split} \text{Real}(\psi(x, t)) = & \frac{1}{\sqrt{2}}\phi_1\cos(\frac{E_1}{\hbar}t)\\&+\frac{1}{\sqrt{2}}\phi_2\cos(\frac{E_2}{\hbar}t) \end{split} \end{equation*}").next_to(phi_1t, DOWN)

		leftData = VGroup(phi_1, phi_1t, Realphi_1t).next_to(box1, 0*DOWN).scale(0.5)
		self.play(Write(leftData[0]))
		self.play(Write(leftData[1]))
		self.play(Write(leftData[2]), run_time = 2)
		self.wait()


		P_1 =  Tex(r"\begin{equation*} \begin{split} \mathbb{P}(x, 0) = & |\psi^*(x, 0)\psi(x, 0)| = \frac{1}{2}\phi_1^2+\frac{1}{2}\phi_2^2+\\ & \phi_1\phi_2 \end{split} \end{equation*}")
		P_1t = Tex(r"\begin{equation*} \begin{split} \mathbb{P}(x, t) = & |\psi^*(x, t)\psi(x, t)| = \frac{1}{2}\phi_1^2+\frac{1}{2}\phi_2^2+\\ & \phi_1\phi_2\cos(\frac{(E_1-E_2)}{\hbar}t) \end{split} \end{equation*}").next_to(P_1, DOWN)
		PIndependent = Text(r"Dependent of time").next_to(P_1t, DOWN)

		rightData = VGroup(P_1, P_1t, PIndependent).next_to(box2, 0*DOWN).scale(0.5)
		self.play(Write(rightData[0]), run_time = 2)
		self.play(Write(rightData[1]), run_time = 2)
		self.play(Write(rightData[2]))


		baseLeftData = Tex(r"$\psi$").next_to(box1, DOWN)
		self.play(leftData.animate.become(baseLeftData))

		baseRightData = Tex(r"$\mathbb{P} = |\psi^*\psi|$").next_to(box2, DOWN)
		self.play(rightData.animate.become(baseRightData))
		self.wait()


		########SuperPosition Animation#############
		self.next_section("Superposition Animation")

		axes = Axes(x_length = 5, x_range= [-0.1, 1.1, 1], y_length = 4.5, y_range = [-6, 6, 2], tips = False)
		axes1 = axes.copy()
		

		axes2 = axes.copy()

		self.play(axes1.animate.shift(3.5*LEFT+0.25*UP), axes2.animate.shift(3.5*RIGHT+0.25*UP))


		baseLine = Line(start = [0, -2, 0], end = [0, 2.5, 0], color = BLACK)
		l1 = baseLine.copy().shift(axes1.c2p([0, 0, 0])[0]*RIGHT)

		l2 = baseLine.copy().shift(axes1.c2p([1, 0, 0])[0]*RIGHT)

		l3 = baseLine.copy().shift(axes2.c2p([0, 0, 0])[0]*RIGHT)

		l4 = baseLine.copy().shift(axes2.c2p([1, 0, 0])[0]*RIGHT)
	
		self.play(Create(l1), Create(l2), Create(l3), Create(l4))


		t = ValueTracker(0)
		leftBaseFunction = axes1.plot(lambda x: (2-0.1)**(0.5)*np.sin(np.pi*x)+(2-0.1)**(0.5)*np.sin(2*np.pi*x), x_range = [0, 1, 0.01], color = BLUE)


		rightBaseFunction = axes2.plot(lambda x: (2-0.1)*np.sin(np.pi*x)*np.sin(np.pi*x)+(2-0.1)*np.sin(2*np.pi*x)*np.sin(2*np.pi*x) + (2-0.1)**(0.5)*np.sin(np.pi*x)*(2-0.1)**(0.5)*np.sin(2*np.pi*x), x_range = [0, 1, 0.01], color = BLUE)

		self.play(Create(leftBaseFunction), Create(rightBaseFunction))

		leftBaseFunction.add_updater(lambda mobject: mobject.become(axes1.plot(lambda x: (2-0.1)**(0.5)*np.sin(np.pi*x)*np.cos(t.get_value())+(2-0.1)**(0.5)*np.sin(2*np.pi*x)*np.cos(4*t.get_value()), x_range = [0, 1, 0.01], color = BLUE)))
		rightBaseFunction.add_updater(lambda mobject: mobject.become(axes2.plot(lambda x: (2-0.1)*np.sin(np.pi*x)*np.sin(np.pi*x)+(2-0.1)*np.sin(2*np.pi*x)*np.sin(2*np.pi*x) + (2-0.1)**(0.5)*np.sin(np.pi*x)*(2-0.1)**(0.5)*np.sin(2*np.pi*x)*np.cos(3*t.get_value()), x_range = [0, 1, 0.01], color = BLUE)))
		self.play(t.animate.set_value(10), run_time = 10, rate_func = linear)
		leftBaseFunction.clear_updaters()
		rightBaseFunction.clear_updaters()
		self.play(FadeOut(axes1, axes2, l1, l2, l3, l4, leftBaseFunction, rightBaseFunction, leftData, rightData, introText, box1, box2), run_time = 2)


