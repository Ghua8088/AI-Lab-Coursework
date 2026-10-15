from abc import ABC, abstractmethod

from abc import ABC, abstractmethod

class GameEnvironment(ABC):
    @abstractmethod
    def get_initial_state(self):
        pass

    @abstractmethod
    def get_current_player(self, state) -> int:
        """Returns +1 (Player 1) or -1 (Player 2)."""
        pass

    @abstractmethod
    def get_legal_actions(self, state) -> list:
        pass

    @abstractmethod
    def apply_action(self, state, action):
        """Returns new immutable state."""
        pass

    @abstractmethod
    def is_terminal(self, state):
        """
        Returns (is_over: bool, utility: float | None)
        Utility is expressed relative to Player +1:
          +1.0 = Player +1 won
          -1.0 = Player -1 won
           0.0 = Draw
        """
        pass

# 2. Universal Base Policy
class Policy(ABC):
    @abstractmethod
    def __call__(self, state, game: GameEnvironment):
        """Returns the chosen action for the given state and game rules."""
        pass
# 3. Lean Agent
class Agent:
    def __init__(self, policy: Policy, name="Agent"):
        self.policy = policy
        self.name = name

    def select_action(self, state, game: GameEnvironment):
        return self.policy(state, game)
class MiniMaxPolicy(Policy):
    def __init__(self, max_depth=3, eval_fn=None):
        self.max_depth = max_depth
        self.eval_fn = eval_fn or (lambda state: 0)

    def __call__(self, state, game: GameEnvironment):
        best_action = None
        best_val = float("-inf")
        alpha, beta = float("-inf"), float("inf")

        for action in game.get_legal_actions(state):
            next_state = game.apply_action(state, action)
            val = self._search(next_state, game, depth=1, is_maximizing=False, alpha=alpha, beta=beta)
            if val > best_val:
                best_val = val
                best_action = action
            alpha = max(alpha, best_val)
        return best_action

    def _search(self, state, game: GameEnvironment, depth, is_maximizing, alpha, beta):
        is_over, score = game.is_terminal(state)
        if is_over:
            return score
        if depth >= self.max_depth:
            return self.eval_fn(state)

        legal_actions = game.get_legal_actions(state)
        if is_maximizing:
            best_val = float("-inf")
            for action in legal_actions:
                next_state = game.apply_action(state, action)
                val = self._search(next_state, game, depth + 1, False, alpha, beta)
                best_val = max(best_val, val)
                alpha = max(alpha, best_val)
                if beta <= alpha:
                    break
            return best_val
        else:
            best_val = float("inf")
            for action in legal_actions:
                next_state = game.apply_action(state, action)
                val = self._search(next_state, game, depth + 1, True, alpha, beta)
                best_val = min(best_val, val)
                beta = min(beta, best_val)
                if beta <= alpha:
                    break
            return best_val


class GreedyBestFirstSearchPolicy(Policy):
    def __init__(self, eval_fn):
        self.eval_fn = eval_fn

    def __call__(self, state, game: GameEnvironment):
        legal_actions = game.get_legal_actions(state)
        if not legal_actions:
            return None

        # Evaluates 1-step lookahead and greedily chooses highest evaluation
        best_action = None
        best_val = float("-inf")
        for action in legal_actions:
            next_state = game.apply_action(state, action)
            is_over, score = game.is_terminal(next_state)
            val = score if is_over else self.eval_fn(next_state)
            if val > best_val:
                best_val = val
                best_action = action
        return best_action
class AStarSearchPolicy(Policy):
    def __init__(self, eval_fn):
        self.eval_fn = eval_fn

    def __call__(self, state, game: GameEnvironment):
        legal_actions = game.get_legal_actions(state)
        if not legal_actions:
            return None

        # Evaluates 1-step lookahead and greedily chooses highest evaluation
        best_action = None
        best_val = float("-inf")
        for action in legal_actions:
            next_state = game.apply_action(state, action)
            is_over, score = game.is_terminal(next_state)
            val = score if is_over else self.eval_fn(next_state)
            if val > best_val:
                best_val = val
                best_action = action
        return best_action
def ttt_heuristic(state):
    """
    Positive score favors X, negative favors O.
    Counts lines where one player can still win while the other hasn't blocked.
    """
    score = 0
    patterns = TicTacToe.WIN_PATTERNS
    for a, b, c in patterns:
        line = (state[a], state[b], state[c])
        x_count = line.count("X")
        o_count = line.count("O")
        
        if x_count > 0 and o_count == 0:
            score += (10 ** (x_count - 1))
        elif o_count > 0 and x_count == 0:
            score -= (10 ** (o_count - 1))
    return score
class TicTacToe(GameEnvironment):
    WIN_PATTERNS = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  
        (0, 4, 8), (2, 4, 6)             
    )

    def get_initial_state(self):
        """State is an immutable tuple of 9 elements: '', 'X', or 'O'."""
        return ("",) * 9

    def get_current_player(self, state):
        """'X' always goes first. Count turns to determine who moves next."""
        x_count = state.count("X")
        o_count = state.count("O")
        return "X" if x_count == o_count else "O"

    def get_legal_actions(self, state):
        is_over, _ = self.is_terminal(state)
        if is_over:
            return []
        return [i for i, cell in enumerate(state) if cell == ""]

    def apply_action(self, state, action):
        """Creates an entirely new tuple state without mutating the original."""
        player = self.get_current_player(state)
        state_list = list(state)
        state_list[action] = player
        return tuple(state_list)

    def is_terminal(self, state):
        for a, b, c in self.WIN_PATTERNS:
            if state[a] == state[b] == state[c] and state[a] != "":
                score = 10 if state[a] == "X" else -10
                return True, score
        if "" not in state:
            return True, 0
        return False, None
# Game & Policies Setup
game = TicTacToe()
state = game.get_initial_state()
agent_x = Agent(policy=MiniMaxPolicy(max_depth=9), name="Minimax (X)")
agent_o = Agent(policy=AStarSearchPolicy(eval_fn=ttt_heuristic), name="A* (O)")

# Match Loop
while True:
    current_player = game.get_current_player(state)
    active_agent = agent_x if current_player == "X" else agent_o

    action = active_agent.select_action(state, game)
    state = game.apply_action(state, action)

    # Render board
    for row in range(3):
        print([state[row * 3 + col] or " " for col in range(3)])
    print("-" * 15)

    is_over, score = game.is_terminal(state)
    if is_over:
        if score == 10:
            print("Minimax (X) Won!")
        elif score == -10:
            print("Greedy (O) Won!")
        else:
            print("Game ended in a Draw!")
        break
