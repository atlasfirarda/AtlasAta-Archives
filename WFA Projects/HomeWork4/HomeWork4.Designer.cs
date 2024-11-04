namespace HomeWork4
{
    partial class HomeWork4
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }

            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.groupAsker = new System.Windows.Forms.GroupBox();
            this.listRecourse = new System.Windows.Forms.ListBox();
            this.buttonRecourse = new System.Windows.Forms.Button();
            this.panel2 = new System.Windows.Forms.Panel();
            this.pickerTarih = new System.Windows.Forms.DateTimePicker();
            this.labelTarih = new System.Windows.Forms.Label();
            this.panel3 = new System.Windows.Forms.Panel();
            this.buttonWoman = new System.Windows.Forms.RadioButton();
            this.buttonMan = new System.Windows.Forms.RadioButton();
            this.labelCinsiyet = new System.Windows.Forms.Label();
            this.panel1 = new System.Windows.Forms.Panel();
            this.textTC = new System.Windows.Forms.TextBox();
            this.labelTC = new System.Windows.Forms.Label();
            this.groupAsker.SuspendLayout();
            this.panel2.SuspendLayout();
            this.panel3.SuspendLayout();
            this.panel1.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupAsker
            // 
            this.groupAsker.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(15)))), ((int)(((byte)(15)))), ((int)(((byte)(15)))));
            this.groupAsker.Controls.Add(this.listRecourse);
            this.groupAsker.Controls.Add(this.buttonRecourse);
            this.groupAsker.Controls.Add(this.panel2);
            this.groupAsker.Controls.Add(this.panel3);
            this.groupAsker.Controls.Add(this.panel1);
            this.groupAsker.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.groupAsker.ForeColor = System.Drawing.Color.White;
            this.groupAsker.Location = new System.Drawing.Point(112, 28);
            this.groupAsker.Name = "groupAsker";
            this.groupAsker.Padding = new System.Windows.Forms.Padding(5);
            this.groupAsker.Size = new System.Drawing.Size(720, 540);
            this.groupAsker.TabIndex = 0;
            this.groupAsker.TabStop = false;
            this.groupAsker.Text = "Askerlik Başvurusu";
            // 
            // listRecourse
            // 
            this.listRecourse.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(25)))), ((int)(((byte)(25)))), ((int)(((byte)(25)))));
            this.listRecourse.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.listRecourse.Cursor = System.Windows.Forms.Cursors.No;
            this.listRecourse.Font = new System.Drawing.Font("Cascadia Code NF", 12.75F);
            this.listRecourse.ForeColor = System.Drawing.Color.White;
            this.listRecourse.FormattingEnabled = true;
            this.listRecourse.ItemHeight = 22;
            this.listRecourse.Location = new System.Drawing.Point(120, 275);
            this.listRecourse.Name = "listRecourse";
            this.listRecourse.Size = new System.Drawing.Size(467, 220);
            this.listRecourse.TabIndex = 5;
            this.listRecourse.TabStop = false;
            // 
            // buttonRecourse
            // 
            this.buttonRecourse.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(25)))), ((int)(((byte)(25)))), ((int)(((byte)(25)))));
            this.buttonRecourse.FlatAppearance.BorderSize = 0;
            this.buttonRecourse.FlatAppearance.MouseDownBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(65)))), ((int)(((byte)(65)))), ((int)(((byte)(65)))));
            this.buttonRecourse.FlatAppearance.MouseOverBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(35)))), ((int)(((byte)(35)))), ((int)(((byte)(35)))));
            this.buttonRecourse.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.buttonRecourse.Location = new System.Drawing.Point(120, 211);
            this.buttonRecourse.Name = "buttonRecourse";
            this.buttonRecourse.Size = new System.Drawing.Size(467, 49);
            this.buttonRecourse.TabIndex = 4;
            this.buttonRecourse.Text = "BAŞVUR";
            this.buttonRecourse.UseVisualStyleBackColor = false;
            this.buttonRecourse.Click += new System.EventHandler(this.buttonRecourse_Click);
            // 
            // panel2
            // 
            this.panel2.Controls.Add(this.pickerTarih);
            this.panel2.Controls.Add(this.labelTarih);
            this.panel2.Location = new System.Drawing.Point(120, 115);
            this.panel2.Name = "panel2";
            this.panel2.Padding = new System.Windows.Forms.Padding(5);
            this.panel2.Size = new System.Drawing.Size(468, 42);
            this.panel2.TabIndex = 1;
            // 
            // pickerTarih
            // 
            this.pickerTarih.CalendarForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(55)))), ((int)(((byte)(55)))), ((int)(((byte)(55)))));
            this.pickerTarih.CalendarMonthBackground = System.Drawing.SystemColors.ActiveBorder;
            this.pickerTarih.CalendarTitleBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(55)))), ((int)(((byte)(55)))), ((int)(((byte)(55)))));
            this.pickerTarih.Cursor = System.Windows.Forms.Cursors.IBeam;
            this.pickerTarih.DropDownAlign = System.Windows.Forms.LeftRightAlignment.Right;
            this.pickerTarih.Format = System.Windows.Forms.DateTimePickerFormat.Short;
            this.pickerTarih.Location = new System.Drawing.Point(183, 5);
            this.pickerTarih.MaxDate = new System.DateTime(2024, 12, 31, 0, 0, 0, 0);
            this.pickerTarih.MinDate = new System.DateTime(1919, 9, 9, 0, 0, 0, 0);
            this.pickerTarih.Name = "pickerTarih";
            this.pickerTarih.ShowUpDown = true;
            this.pickerTarih.Size = new System.Drawing.Size(277, 34);
            this.pickerTarih.TabIndex = 1;
            this.pickerTarih.Value = new System.DateTime(2008, 11, 4, 3, 0, 0, 0);
            // 
            // labelTarih
            // 
            this.labelTarih.Cursor = System.Windows.Forms.Cursors.No;
            this.labelTarih.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.labelTarih.Location = new System.Drawing.Point(8, 5);
            this.labelTarih.Name = "labelTarih";
            this.labelTarih.Size = new System.Drawing.Size(169, 32);
            this.labelTarih.TabIndex = 0;
            this.labelTarih.Text = "Doğum Tarihi";
            // 
            // panel3
            // 
            this.panel3.Controls.Add(this.buttonWoman);
            this.panel3.Controls.Add(this.buttonMan);
            this.panel3.Controls.Add(this.labelCinsiyet);
            this.panel3.Location = new System.Drawing.Point(120, 163);
            this.panel3.Name = "panel3";
            this.panel3.Padding = new System.Windows.Forms.Padding(5);
            this.panel3.Size = new System.Drawing.Size(468, 42);
            this.panel3.TabIndex = 1;
            // 
            // buttonWoman
            // 
            this.buttonWoman.Cursor = System.Windows.Forms.Cursors.Hand;
            this.buttonWoman.Font = new System.Drawing.Font("Cascadia Code NF", 15.25F);
            this.buttonWoman.Location = new System.Drawing.Point(299, 5);
            this.buttonWoman.Name = "buttonWoman";
            this.buttonWoman.Size = new System.Drawing.Size(93, 29);
            this.buttonWoman.TabIndex = 3;
            this.buttonWoman.Text = "KADIN";
            this.buttonWoman.UseVisualStyleBackColor = true;
            // 
            // buttonMan
            // 
            this.buttonMan.Checked = true;
            this.buttonMan.Cursor = System.Windows.Forms.Cursors.Hand;
            this.buttonMan.Font = new System.Drawing.Font("Cascadia Code NF", 15.25F);
            this.buttonMan.Location = new System.Drawing.Point(202, 5);
            this.buttonMan.Name = "buttonMan";
            this.buttonMan.Size = new System.Drawing.Size(91, 32);
            this.buttonMan.TabIndex = 2;
            this.buttonMan.TabStop = true;
            this.buttonMan.Text = "ERKEK";
            this.buttonMan.UseVisualStyleBackColor = true;
            // 
            // labelCinsiyet
            // 
            this.labelCinsiyet.Cursor = System.Windows.Forms.Cursors.No;
            this.labelCinsiyet.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.labelCinsiyet.Location = new System.Drawing.Point(8, 5);
            this.labelCinsiyet.Name = "labelCinsiyet";
            this.labelCinsiyet.Size = new System.Drawing.Size(134, 32);
            this.labelCinsiyet.TabIndex = 0;
            this.labelCinsiyet.Text = "Cinsiyet";
            // 
            // panel1
            // 
            this.panel1.Controls.Add(this.textTC);
            this.panel1.Controls.Add(this.labelTC);
            this.panel1.Location = new System.Drawing.Point(120, 67);
            this.panel1.Name = "panel1";
            this.panel1.Padding = new System.Windows.Forms.Padding(5);
            this.panel1.Size = new System.Drawing.Size(468, 42);
            this.panel1.TabIndex = 1;
            // 
            // textTC
            // 
            this.textTC.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(35)))), ((int)(((byte)(35)))), ((int)(((byte)(35)))));
            this.textTC.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.textTC.ForeColor = System.Drawing.Color.White;
            this.textTC.Location = new System.Drawing.Point(148, 5);
            this.textTC.MaxLength = 11;
            this.textTC.Multiline = true;
            this.textTC.Name = "textTC";
            this.textTC.Size = new System.Drawing.Size(312, 32);
            this.textTC.TabIndex = 0;
            // 
            // labelTC
            // 
            this.labelTC.Cursor = System.Windows.Forms.Cursors.No;
            this.labelTC.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.labelTC.Location = new System.Drawing.Point(8, 5);
            this.labelTC.Name = "labelTC";
            this.labelTC.Size = new System.Drawing.Size(134, 32);
            this.labelTC.TabIndex = 0;
            this.labelTC.Text = "TC Kimlik";
            // 
            // HomeWork4
            // 
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.None;
            this.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(10)))), ((int)(((byte)(10)))), ((int)(((byte)(10)))));
            this.ClientSize = new System.Drawing.Size(920, 620);
            this.Controls.Add(this.groupAsker);
            this.Font = new System.Drawing.Font("Cascadia Code NF", 17.25F);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.KeyPreview = true;
            this.Margin = new System.Windows.Forms.Padding(7, 6, 7, 6);
            this.Name = "HomeWork4";
            this.Padding = new System.Windows.Forms.Padding(5);
            this.Text = "HomeWork4";
            this.Load += new System.EventHandler(this.HomeWork4_Load);
            this.KeyDown += new System.Windows.Forms.KeyEventHandler(this.onKeyPreview);
            this.groupAsker.ResumeLayout(false);
            this.panel2.ResumeLayout(false);
            this.panel3.ResumeLayout(false);
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            this.ResumeLayout(false);
        }

        private System.Windows.Forms.ListBox listRecourse;

        private System.Windows.Forms.Button buttonRecourse;

        private System.Windows.Forms.RadioButton buttonWoman;

        private System.Windows.Forms.RadioButton buttonMan;

        private System.Windows.Forms.Panel panel3;
        private System.Windows.Forms.Label labelCinsiyet;

        private System.Windows.Forms.DateTimePicker pickerTarih;

        private System.Windows.Forms.TextBox textTC;
        private System.Windows.Forms.Panel panel2;
        private System.Windows.Forms.Label labelTarih;

        private System.Windows.Forms.TextBox textTarih;

        private System.Windows.Forms.Panel panel1;

        private System.Windows.Forms.Label labelTC;

        private System.Windows.Forms.GroupBox groupAsker;

        #endregion
    }
}