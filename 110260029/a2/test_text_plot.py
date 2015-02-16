from text_plot import plot

def test_text_plot():
    assert __unique([1,1,1])==[1]
    assert __unique([1,2,3])==[1,2,3]
    assert __createline([1],3)==" * "
    assert __createline([1,2],5)==" **  "

if __name__=="__main__":
    test_text_plot()
