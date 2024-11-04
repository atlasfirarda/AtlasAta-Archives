using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Windows.Forms.VisualStyles;

namespace HomeWork4
{
    public partial class HomeWork4 : Form
    {
        public HomeWork4()
        {
            InitializeComponent();
        }

        private void HomeWork4_Load(object sender, EventArgs e)
        {
            textTC.Focus();
            pickerTarih.Value = DateTime.Now;
        }

        private void onKeyPreview(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Escape)
            {
                this.Close();
            }
        }


        private static int thisYear = DateTime.Now.Year; 
        
        private void buttonRecourse_Click(object sender, EventArgs e)
        {
            string text = textTC.Text;
            int inputYear = pickerTarih.Value.Year;
            int age = thisYear - inputYear;
            double inputText;

            char cinsiyet;

            if (buttonMan.Checked)
                cinsiyet = 'e';
            else
                cinsiyet = 'k';

            if (text.Length > 0 && text.Length == 11 && double.TryParse(text, out inputText))
            {
                if (age >= 20 )
                {
                    if (cinsiyet == 'e')
                    {
                        if (!listRecourse.Items.Contains(text))
                        {
                            listRecourse.Items.Add(text);
                        }
                    }
                    else
                    {
                        MessageBox.Show("Maalesef erkek olmalısınız.", "Hata", MessageBoxButtons.OK, MessageBoxIcon.Error);
                        textTC.Clear();
                        pickerTarih.Value = DateTime.Now;
                    }
                        
                }
                else
                {
                    MessageBox.Show("Maalesef yaşınız yetmiyor.", "Hata", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    textTC.Clear();
                    pickerTarih.Value = DateTime.Now;
                }
            }
            else
            {
                MessageBox.Show("Lütfen doğru bir tc kimlik giriniz.", "Hata", MessageBoxButtons.OK, MessageBoxIcon.Error);
                textTC.Clear();
                textTC.Focus();
            }



        }
    }
}