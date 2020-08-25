from unittest.mock import Mock, patch

from app.vat_calculator import VatCalculator


# Examples
def spec__list():
    """spec as a list"""
    mock = Mock(spec=['method1', 'method2'])
    print(dir(mock))
    print(mock.method1)
    print(mock.method2)
    # print(mock.method3)
    mock.method3 = lambda: 1
    print(mock.method3())


def spec_set__list():
    """spec_set as a list"""
    mock = Mock(spec_set=['method1', 'method2'])
    print(dir(mock))
    print(mock.method1)
    print(mock.method2)
    # print(mock.method3)
    # mock.method3 = lambda: 1


class MockedCalc:
    def method1(self, net):
        return net * 45.2233


def spec__object():
    """spec as an object"""
    mock = Mock(spec=MockedCalc)
    print(dir(mock))
    print(mock.method1)
    # print(mock.method3)
    mock.method3 = lambda: 1
    print(mock.method3())


def side_effect_example(x):
    return x ** 0.5


def side_effect__func():
    """side_effect function"""
    mock = Mock(side_effect=side_effect_example)
    print(mock(121))


def side_effect__iterable():
    """side_effect iterable"""
    mock = Mock(side_effect=(1, 2, 3))
    print(mock())
    print(mock())
    print(mock())
    # print(mock())


def side_effect__exception():
    """side_effect exception"""
    mock = Mock(side_effect=TypeError)
    try:
        mock()
    except TypeError:
        print('An error occurred.')


def return_value():
    """return_value"""
    mock = Mock(return_value='Dzień dobry Wojtek!')
    print(mock())


def wraps():
    """wraps"""
    vc = VatCalculator(23)

    # 1: Wrap the whole object
    spy = Mock(wraps=vc)
    print(spy.net_vat(123))
    spy.net_vat.assert_called_once_with(123)
    # spy.net.assert_called_once_with(123)

    # 2: Just wrap net and let it execute normally
    with patch('app.main.VatCalculator.net') as mock:
        print(vc.net_vat(123))
        mock.assert_called_once_with(123)

    with patch('app.main.VatCalculator.net', wraps=vc.net) as mock:
        print(vc.net_vat(123))
        mock.assert_called_once_with(123)


def unsafe():
    """unsafe"""
    mock = Mock(unsafe=True)
    print(mock.assert_not_call)
    mock = Mock()
    try:
        print(mock.assert_not_call)
    except AttributeError as e:
        print(f'Method \'{e}\' doesn\'t exist.')


def kwargs():
    """kwargs"""
    mock = Mock(param1=10, param2='Hello!')
    print(mock.param1)
    print(mock.param2)
    print(mock.param3)


def patch_context_manager():
    """patch a a context manager"""
    with patch('app.main.VatCalculator') as mock:
        print(mock.net(12))


def patch_new():
    """patch new"""
    with patch('app.main.VatCalculator', new=MockedCalc()) as mock:
        print(mock.method1(10))
        # print(mock.net(10))


def patch_create():
    """patch create"""
    try:
        with patch('app.main.VatCalculator.non_existing_attr') as mock:
            print(mock)
    except AttributeError as e:
        print(e)

    with patch('app.main.VatCalculator.non_existing_attr', create=True) as mock:
        print(mock)
        print(mock.non_existing_attr)


def patch_autospec():
    """patch autospec"""
    with patch('app.main.VatCalculator') as mock:
        print(mock.gross(20))
        print(mock.foo(124))

    with patch('app.main.VatCalculator', autospec=True) as mock:
        print(mock.gross(20))
        try:
            print(mock.foo(124))
        except AttributeError as e:
            print(e)


def patch_new_callable():
    """patch new_callable"""
    with patch('app.main.VatCalculator', new_callable=MockedCalc) as mock:
        print(mock.method1(10))
        # print(mock.net(10))


@patch('app.main.VatCalculator')
def patch_decorator(mock):
    """patch decorator"""
    print(mock)


@patch('app.main.MockedCalc', autospec=True)
@patch('app.main.VatCalculator', autospec=True)
def patch_multiple_decorators(mock_vc, mock_mc):
    """patch multiple decorators"""
    print(mock_vc)
    print(mock_vc.gross(100))
    print(mock_mc)
    print(mock_mc.method1(100))
    # print(mock_mc.gross(123))


if __name__ == '__main__':
    counter = 1
    for f in (
            spec__list,
            spec_set__list,
            spec__object,
            side_effect__func,
            side_effect__iterable,
            side_effect__exception,
            return_value,
            wraps,
            unsafe,
            kwargs,
            patch_context_manager,
            patch_new,
            patch_create,
            patch_autospec,
            patch_new_callable,
            patch_decorator,
            patch_multiple_decorators,
    ):
        print(f'EXAMPLE {counter}:', f.__doc__)
        f()
        print()
        counter += 1
