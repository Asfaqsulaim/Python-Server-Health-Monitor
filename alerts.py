
def check_usage(metric , usage , limit):
    if usage > limit:
        if metric == "CPU":
            return (f"Warning: {metric} usage is {usage}% |Allowed Limit:{limit}% | Action required: Optimize CPU usage.")
        elif metric == "RAM":
            return (f"Warning: {metric} usage is {usage}% |Allowed Limit:{limit}% | Action required: Close unnecessary applications.")
        elif metric == "Disk":
            return (f"Warning: {metric} usage is {usage}% |Allowed Limit:{limit}% | Action required: Free up Disk Space.")  
        return (f"Warning: {metric} usage is {usage}% |Allowed Limit:{limit}% | Please take action.")
    else:
        return (f"Normal: {metric} usage is {usage}% |Allowed Limit:{limit}% | No action needed.")