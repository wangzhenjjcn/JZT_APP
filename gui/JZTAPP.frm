VERSION 5.00
Begin VB.Form JZTAPP 
   Caption         =   "九州通数据采集系统"
   ClientHeight    =   11010
   ClientLeft      =   180
   ClientTop       =   465
   ClientWidth     =   19080
   LinkTopic       =   "Form1"
   ScaleHeight     =   11010
   ScaleWidth      =   19080
   StartUpPosition =   3  '窗口缺省
   Begin VB.Frame Data 
      Caption         =   "数据"
      Height          =   10815
      Left            =   4920
      TabIndex        =   1
      Top             =   120
      Width           =   13935
      Begin VB.Frame QuickViewFrame 
         Caption         =   "快速浏览"
         Height          =   2895
         Left            =   5040
         TabIndex        =   11
         Top             =   240
         Width           =   8055
         Begin VB.PictureBox Picture1 
            Height          =   2000
            Left            =   360
            ScaleHeight     =   1935
            ScaleWidth      =   1935
            TabIndex        =   12
            Top             =   480
            Width           =   2000
         End
         Begin VB.Label Label2 
            Caption         =   "品名"
            Height          =   255
            Left            =   2880
            TabIndex        =   15
            Top             =   1440
            Width           =   4995
         End
         Begin VB.Label Label1 
            Caption         =   "品名"
            Height          =   255
            Left            =   2880
            TabIndex        =   14
            Top             =   960
            Width           =   4995
         End
         Begin VB.Label QuickViewName 
            Caption         =   "品名"
            Height          =   255
            Left            =   2880
            TabIndex        =   13
            Top             =   480
            Width           =   5000
         End
      End
      Begin VB.TextBox SearchKeywordText 
         Height          =   400
         Left            =   1440
         TabIndex        =   9
         Text            =   "在这里输入你要搜索的药物名称"
         Top             =   1920
         Width           =   2895
      End
      Begin VB.ComboBox SortComboThree 
         Height          =   300
         Left            =   2040
         TabIndex        =   7
         Text            =   "Combo1"
         Top             =   1440
         Width           =   2295
      End
      Begin VB.ComboBox SortComboTwo 
         Height          =   300
         Left            =   2040
         TabIndex        =   5
         Text            =   "Combo1"
         Top             =   960
         Width           =   2295
      End
      Begin VB.ComboBox SortComboOne 
         Height          =   300
         Left            =   2040
         TabIndex        =   3
         Text            =   "Combo1"
         Top             =   480
         Width           =   2295
      End
      Begin VB.ListBox List1 
         Height          =   7980
         Left            =   240
         TabIndex        =   2
         Top             =   2640
         Width           =   4095
      End
      Begin VB.Label SearchKeyWordLable 
         Caption         =   "检索关键字:"
         Height          =   255
         Left            =   240
         TabIndex        =   10
         Top             =   1920
         Width           =   1095
      End
      Begin VB.Label SortLableThree 
         Caption         =   "药品分类3:"
         Height          =   255
         Left            =   240
         TabIndex        =   8
         Top             =   1440
         Width           =   1095
      End
      Begin VB.Label SortLableTwo 
         Caption         =   "药品分类2:"
         Height          =   255
         Left            =   240
         TabIndex        =   6
         Top             =   960
         Width           =   1095
      End
      Begin VB.Label SortLableOne 
         Caption         =   "药品分类1:"
         Height          =   255
         Left            =   240
         TabIndex        =   4
         Top             =   480
         Width           =   1095
      End
   End
   Begin VB.Frame Info 
      Caption         =   "设置"
      Height          =   10815
      Left            =   120
      TabIndex        =   0
      Top             =   120
      Width           =   4695
   End
End
Attribute VB_Name = "JZTAPP"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
