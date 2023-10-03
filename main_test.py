import random

from main import main


def test_free1(capsys, monkeypatch):
    amount = random.randrange(100000, 324999)
    inputs = iter([str(amount), '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert captured.out == 'Tax: 0\n'

def test_free2(capsys, monkeypatch):
    amount = random.randrange(325000, 999999)
    inputs = iter([str(amount), '7'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert captured.out == 'Tax: 0\n'

def test_40(capsys, monkeypatch):
    amount = random.randrange(325000, 999999)
    tax = (amount - 325000) * 0.4
    inputs = iter([str(amount), '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert captured.out == f'Tax: {tax}\n'

def test_32(capsys, monkeypatch):
    amount = random.randrange(325000, 999999)
    tax = (amount - 325000) * 0.32
    inputs = iter([amount, 3.5])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert captured.out == f'Tax: {tax}\n'


def test_24(capsys, monkeypatch):
    amount = random.randrange(325000, 999999)
    tax = (amount - 325000) * 0.24
    inputs = iter([str(amount), '4.1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert captured.out == f'Tax: {tax}\n'


def test_16(capsys, monkeypatch):
    amount = random.randrange(325000, 999999)
    tax = (amount - 325000) * 0.16
    inputs = iter([str(amount), '5.75'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert captured.out == f'Tax: {tax}\n'


def test_8(capsys, monkeypatch):
    amount = random.randrange(325000, 999999)
    tax = (amount - 325000) * 0.08
    inputs = iter([str(amount), '6.25'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert captured.out == f'Tax: {tax}\n'
