# vote_manager.py
from Project1 import config


def record_vote(voter_id: str, candidate_id: int, votes):
    if voter_id in votes:
        return "already_voted"
    else:
        votes[voter_id] = config.CANDIDATES[candidate_id]
        with open(config.VOTER_FILE, 'a') as file:
            file.write(f"{voter_id}: {config.CANDIDATES[candidate_id]}\n")
        return f"voted_for_{candidate_id}"

def validate_voter_id(voter_id: str) -> bool:
    # Check if the voter ID is numeric
    return voter_id.isdigit()




