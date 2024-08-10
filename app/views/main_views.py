from flask import Blueprint, render_template

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def intro():
    return render_template('intro.html')

@bp.route('/calendar')
def calendar():
    return render_template('calendar.html')

@bp.route('/login')
def login():
    return render_template('login.html')

@bp.route('/regist')
def regist():
    return render_template('regist.html')

@bp.route('/home')
def home():
    return render_template('home.html')

@bp.route('/board')
def board():
    return render_template('board.html')

@bp.route('/plan')
def plan():
    return render_template('plan.html')

@bp.route('/contest')
def contest():
    return render_template('contest.html')

@bp.route('/notice')
def notice():
    return render_template('notice.html')

@bp.route('/mypage')
def mypage():
    return render_template('mypage.html')

@bp.route('/write')
def write():
    return render_template('write.html')

@bp.route('/planing')
def planing():
    return render_template('planing.html')

@bp.route('/plan/<int:plan_id>/')
def plan_act(plan_id):
    plan = Plan.query.get(plan_id)
    return render_template('plan/plan_detail.html', plan=plan)

@bp.route('/board/<int:board_id>/')
def board_act(board_id):
    board = Board.query.get(board_id)
    return render_template('board/board_detail.html', board=board)

@bp.route('/notice/<int:notice_id>/')
def notice_act(notice_id):
    notice = Notice.query.get(notice_id)
    return render_template('notice/notice_detail.html', notice=notice)