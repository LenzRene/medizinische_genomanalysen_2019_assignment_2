#! /usr/bin/env python3

import vcf

__author__ = 'Rene Lenz'


class Assignment2:
    
    def __init__(self):
        ## Check if pyvcf is installed
        print("PyVCF version: %s" % vcf.VERSION)
        

    def get_average_quality_of_file(self):
        '''
        Get the average PHRED quality of all variants
        :return:
        '''    
        quality = 0
        counter = 0
        with open("chr22_new.vcf") as my_vcf_fh:
            vcf_reader = vcf.Reader(my_vcf_fh)
            for record in vcf_reader:
                quality = quality + record.QUAL
                counter += 1
                avg_quality = quality / counter
        print("Average quality of the variants is: ", avg_quality)
        #return avg_quality
        
        
    def get_total_number_of_variants_of_file(self):
        '''
        Get the total number of variants
        :return: total number of variants
        '''
        #grep '^chr22' chr22.vcf | wc -l
        v_counter = 0
        with open("chr22_new.vcf") as my_vcf_fh:
            vcf_reader = vcf.Reader(my_vcf_fh)
            for record in vcf_reader:
                v_counter +=  1
        return(v_counter)
        #print("Total Number of Variants: ", v_counter)
    
    
    def get_variant_caller_of_vcf(self):
        '''
        Return the variant caller name
        :return: 
        '''
        caller_set = set()
        with open("chr22_new.vcf") as my_vcf_fh:
            vcf_reader = vcf.Reader(my_vcf_fh)
            for record in vcf_reader:
                info = record.INFO["callsetnames"]
                for i in range(len(info)):
                    caller_set.add(info[i])
        print(" Variant caller: ", caller_set)
        #return caller_set
        
        
    def get_human_reference_version(self):
        '''
        Return the genome reference version
        :return: 
        '''
        with open("chr22_new.vcf") as my_vcf_fh:
            vcf_reader = vcf.Reader(my_vcf_fh)
            for record in vcf_reader:
                info = record.INFO["difficultregion"] # Liste ... 1
                reference_version = info[0] # Neue Variable für den Eintrag
                print(reference_version[0:4])
                break

    def get_number_of_indels(self):
        '''
        Return the number of identified INDELs
        :return:
        '''
        indel_counter = 0
        with open("chr22_new.vcf") as my_vcf_fh:
            vcf_reader = vcf.Reader(my_vcf_fh)
            for record in vcf_reader:
                if record.is_indel:
                    indel_counter +=  1
        return(indel_counter)


    def get_number_of_snvs(self):
        '''
        Return the number of SNVs
        :return: 
        ''' 
        snv_counter = 0
        with open("chr22_new.vcf") as my_vcf_fh:
            vcf_reader = vcf.Reader(my_vcf_fh)
            for record in vcf_reader:
                if record.is_snp:
                    snv_counter = snv_counter + 1
        return(snv_counter)
        #print("Number of snv: ", snv_counter)
        
    def get_number_of_heterozygous_variants(self):
        '''
        Return the number of heterozygous variants
        :return: 
        '''
        with open("chr22_new.vcf") as my_vcf_fh:
            het_counter = 0
            vcf_reader = vcf.Reader(my_vcf_fh)
            for record in vcf_reader:
                if record.num_het:
                    het_counter += 1

            #return(vcf_reader.num_het)
        return(het_counter)
        
    
    def merge_chrs_into_one_vcf(self):
        '''
        Creates one VCF containing all variants of chr21 and chr22
        :return:
        '''

        file = open("chr21_new.vcf")
        w_f = open("newfile2.vcf", "w+")
        linesFirstFile = 0
        for line in file:
            w_f.write(line)
            linesFirstFile+=1
        file.close
        w_f.close
        print("lines of first file: ", linesFirstFile)

        file = open("chr22_new.vcf")
        w_f = open("newfile2.vcf", "a")
        linesSecondFile = 0
        for line in file:
            w_f.write(line)
            linesSecondFile +=1
        file.close
        w_f.close

        print("lines of second file: ", linesSecondFile)
        lineSum = linesFirstFile + linesSecondFile
        print("sum of merged lines: ", lineSum)


    def print_summary(self):
        self.get_average_quality_of_file()
        print("Total Number of Variants: ", self.get_total_number_of_variants_of_file())
        self.get_variant_caller_of_vcf()
        print("human ref.: ", self.get_human_reference_version())
        print("Number of INDELs", self.get_number_of_indels())
        print("Number of SNVS: ", self.get_number_of_snvs())
        print("Number of Heterozygous Variants: ", self.get_number_of_heterozygous_variants())
        self.merge_chrs_into_one_vcf()
    
    
def main():
    print("Assignment 2")
    assignment2 = Assignment2()
    assignment2.print_summary()
    print("Done with assignment 2")

if __name__ == '__main__':
main()