import LMRenderer
import LMState

renderer = LMRenderer(81, 18)
testState = LMState(9, 9)

renderer.renderLEDMatrix(testState)