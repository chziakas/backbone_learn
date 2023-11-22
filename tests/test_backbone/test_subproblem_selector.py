import numpy as np

from backbone_learn.backbone.subproblem_feature_selector import SubproblemFeatureSelector


def test_subproblem_feature_selector_initialization():
    utilities = np.array([0.1, 0.4, 0.6, 0.3])
    num_features_to_select = 2
    selector = SubproblemFeatureSelector(utilities, num_features_to_select)

    if not np.array_equal(selector.utilities, utilities):
        raise AssertionError("Selector utilities not set correctly")
    if selector.num_features_to_select != num_features_to_select:
        raise AssertionError("Selector num_features_to_select not set correctly")


def test_subproblem_feature_selector_selection():
    utilities = np.array([0.1, 0.4, 0.6, 0.3])
    num_features_to_select = 2
    selector = SubproblemFeatureSelector(utilities, num_features_to_select)

    selected_indices = selector.select()

    # Check if the length of the selected indices is correct
    if len(selected_indices) != num_features_to_select:
        raise AssertionError("Incorrect number of features selected")

    # Check if selected indices are valid
    if not all([idx in range(len(utilities)) for idx in selected_indices]):
        raise AssertionError("Invalid indices selected")


def test_subproblem_feature_selector_probability_distribution():
    utilities = np.array([0, 10, 20, 30])
    num_features_to_select = 1
    selector = SubproblemFeatureSelector(utilities, num_features_to_select)

    selector.select()

    # Run the selection multiple times to verify distribution
    counts = np.zeros(len(utilities))
    for _ in range(1000):
        idx = selector.select()[0]
        counts[idx] += 1

    if np.argmax(counts) != np.argmax(utilities):
        raise AssertionError("Probability distribution does not align with utility values")
