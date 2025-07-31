import argparse
import sys
import pytest

from config import *
from main import parse_arguments, positive_float
from sort import sort


def test_heavy_package_mass():
    stack = sort(width=10, height=10, lenght=10, mass=20)
    assert stack == SPECIAL_STACK

def test_bulky_package():
    stack = sort(width=100, height=100, lenght=100, mass=15)
    assert stack == SPECIAL_STACK

def test_bulky_and_heavy_package():
    stack = sort(width=100, height=100, lenght=100, mass=21)
    assert stack == REJECTED_STACK

def test_standard_package():
    stack = sort(width=10, height=10, lenght=2, mass=10)
    assert stack == STANDARD_STACK

def test_negatives_mass_values_to_argparse(monkeypatch, capsys):
    test_args = ['-w' , '10', '-e', '10', '-l', '10', '-m', '-10']
    monkeypatch.setattr(sys, 'argv', test_args)

    with pytest.raises(SystemExit):
        parse_arguments()

    captured = capsys.readouterr()
    assert "must be >0" in captured.err

def test_null_mass_values_to_argparse(monkeypatch, capsys):
    test_args = ['-w' , '10', '-e', '10', '-l', '10', '-m', '0']
    monkeypatch.setattr(sys, 'argv', test_args)

    with pytest.raises(SystemExit):
        parse_arguments()

    captured = capsys.readouterr()
    assert "must be >0" in captured.err

def test_negatives_lenght_values_to_argparse(monkeypatch, capsys):
    test_args = ['-w' , '10', '-e', '10', '-l', '-9', '-m', '10']
    monkeypatch.setattr(sys, 'argv', test_args)

    with pytest.raises(SystemExit):
        parse_arguments()

    captured = capsys.readouterr()
    assert "must be >0" in captured.err

def test_null_lenght_values_to_argparse(monkeypatch, capsys):
    test_args = ['-w' , '10', '-e', '10', '-l', '0', '-m', '10']
    monkeypatch.setattr(sys, 'argv', test_args)

    with pytest.raises(SystemExit):
        parse_arguments()

    captured = capsys.readouterr()
    assert "must be >0" in captured.err

def test_negatives_height_values_to_argparse(monkeypatch, capsys):
    test_args = ['-w' , '10', '-e', '-10', '-l', '10', '-m', '10']
    monkeypatch.setattr(sys, 'argv', test_args)

    with pytest.raises(SystemExit):
        parse_arguments()

    captured = capsys.readouterr()
    assert "must be >0" in captured.err

def test_null_height_values_to_argparse(monkeypatch, capsys):
    test_args = ['-w' , '10', '-e', '0', '-l', '10', '-m', '9']
    monkeypatch.setattr(sys, 'argv', test_args)

    with pytest.raises(SystemExit):
        parse_arguments()

    captured = capsys.readouterr()
    assert "must be >0" in captured.err

def test_negatives_width_values_to_argparse(monkeypatch, capsys):
    test_args = ['-e', '10', '-w', '-10', '-l', '10', '-m', '10']
    monkeypatch.setattr(sys, 'argv', test_args)

    with pytest.raises(SystemExit):
        parse_arguments()

    captured = capsys.readouterr()
    assert "must be >0" in captured.err

def test_null_width_values_to_argparse(monkeypatch, capsys):
    test_args = ['-e', '10', '-w', '0', '-l', '10', '-m', '10']
    monkeypatch.setattr(sys, 'argv', test_args)

    with pytest.raises(SystemExit):
        parse_arguments()

    captured = capsys.readouterr()
    assert "must be >0" in captured.err

def test_non_numerical_values_to_argparse(monkeypatch, capsys):
    test_args = ['-w', '10' , '-e', 'a', '-l', '10', '-m', '10']
    monkeypatch.setattr(sys, 'argv', test_args)

    with pytest.raises(SystemExit):
        parse_arguments()

    captured = capsys.readouterr()
    assert "is not a valid quantity" in captured.err

def test_positive_float_with_non_numeric():
    with pytest.raises(argparse.ArgumentTypeError) as exc_info:
        positive_float('a')
    assert "is not a valid quantity" in str(exc_info.value)

def test_positive_float_with_negative():
    with pytest.raises(argparse.ArgumentTypeError) as exc_info:
        positive_float(-3)
    assert "must be >0" in str(exc_info.value)

def test_positive_float_with_valid_number():
    assert positive_float("3.5") == 3.5
    assert positive_float(2) == 2.0
