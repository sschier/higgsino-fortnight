def divideAndErrors(num_list, num_err_list, denom_list, denom_err_list):

    divs = []
    errs = []

    for n, ne, d, de in zip(num_list, num_err_list, denom_list, denom_err_list):
        dividend = float(n/d)
        dev_large = float(n+ne)/(d-de)
        dev_small = float(n-ne)/(d+de)
        err_high = dev_large-dividend
        err_low = dividend-dev_small
        err = err_high if err_high > err_low else err_low
        divs.append(dividend)
        errs.append(err)
        print "& %.3f $\pm$ %.3f" % (dividend, err)
    return divs, errs

def divideAndError(n, ne, d, de):

    print n, ne, d, de
    dividend = float(n/d)
    dev_large = float(n+ne)/(d-de)
    dev_small = float(n-ne)/(d+de)
    err_high = dev_large-dividend
    err_low = dividend-dev_small
    err = err_high if err_high > err_low else err_low

    return dividend, err


