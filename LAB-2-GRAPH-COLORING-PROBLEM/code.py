colors = [&#39;Red&#39;, &#39;Green&#39;, &#39;Blue&#39;]
states = [&#39;WA&#39;, &#39;NT&#39;, &#39;SA&#39;, &#39;Q&#39;, &#39;NSW&#39;, &#39;V&#39;, &#39;T&#39;]
neighbors = {}
neighbors[&#39;WA&#39;] = [&#39;NT&#39;, &#39;SA&#39;]
neighbors[&#39;NT&#39;] = [&#39;WA&#39;, &#39;SA&#39;, &#39;Q&#39;]
neighbors[&#39;SA&#39;] = [&#39;WA&#39;, &#39;NT&#39;, &#39;Q&#39;, &#39;NSW&#39;, &#39;V&#39;]
neighbors[&#39;Q&#39;] = [&#39;NT&#39;, &#39;SA&#39;, &#39;NSW&#39;]
neighbors[&#39;NSW&#39;] = [&#39;SA&#39;, &#39;Q&#39;, &#39;V&#39;]
neighbors[&#39;V&#39;] = [&#39;SA&#39;, &#39;NSW&#39;]
neighbors[&#39;T&#39;] = []
colors_of_states = {}
def promising(state, color):
for neighbor in neighbors.get(state):
color_of_neighbor = colors_of_states.get(neighbor)
if color_of_neighbor == color:
return False

return True
def get_color_for_state(state):
for color in colors:
if promising(state, color):
return color
def main():
for state in states:
colors_of_states[state] = get_color_for_state(state)
print (colors_of_states)

main()
