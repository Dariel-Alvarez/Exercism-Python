def proverb(*inputs, qualifier):

    if not inputs:
        return []

    proverb = []

    for first, second in zip(inputs, inputs[1:]):
        proverb.append(f"For want of a {first} the {second} was lost.")
    
    if qualifier:
        proverb.append(f"And all for the want of a {qualifier} {inputs[0]}.")
    else:
        proverb.append(f"And all for the want of a {inputs[0]}.")


    return proverb
