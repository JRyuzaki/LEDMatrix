import LMRenderer
import LMState

renderer = LMRenderer.LMRenderer(81, 18)
testState = LMState.LMState(9, 9)

renderer.renderLEDMatrix(testState)