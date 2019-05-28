import numpy as np


def anipolevals(t, y, x):
    """ Evaluation of interpolation polynomials with Aitken-Neville scheme.
        Version for scalar x.
    """
    for i in range(len(y)):
        for k in range(i - 1, -1, -1):
            y[k] = y[k + 1] + (y[k + 1] - y[k]) * (x - t[i]) / (t[i] - t[k])
    return y[0]


def anipoleval(t, y, x):
    """ Evaluation of interpolation polynomials with Aitken-Neville scheme.
        Generic version for scalar or vector x.
    """
    x = np.asanyarray(x)
    y = np.repeat(y[:, np.newaxis], x.size, axis=1)
    for i in range(y.shape[0]):
        for k in range(i - 1, -1, -1):
            y[k, :] = y[k + 1, :] + ((y[k + 1, :] - y[k, :]) *
                                     (x - t[i]) / (t[i] - t[k]))
    return np.asscalar(y[0, :]) if x.size == 1 else y[0, :]


def main():
    # Aproxima d/dx sin(x) con Aitken-Neville y exptrapolacion a 0
    x = 2 * np.pi

    def df(h):
        return (np.sin(x + h) - np.sin(x)) / h

    exact = np.cos(x)
    print('Exact value: {:7.5}'.format(exact))

    for n in range(2, 50, 2):
        # Interpolate for large h
        t = np.linspace(0.01, 10, n)
        y = df(t)

        approx = anipoleval(t, y, 0)
        print('Approximation at n = {:2}: {:15}'.format(n, approx))


if __name__ == '__main__':
    main()
