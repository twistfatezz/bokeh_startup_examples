from bokeh.io import show
from bokeh.models import Panel, Tabs
from bokeh.plotting import figure

p1 = figure(width=300, height=300)
p1.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5)
tab1 = Panel(child=p1, title="circle")

p2 = figure(width=300, height=300)
p2.line([100, 200, 300, 400, 500], [600, 700, 200, 400, 500], line_width=3, color="navy", alpha=0.5)
tab2 = Panel(child=p2, title="line")

show(Tabs(tabs=[tab1, tab2]))
